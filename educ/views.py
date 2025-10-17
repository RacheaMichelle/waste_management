from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import QuizQuestion, QuizScore  # Only import from educ models
# Import Resource from education app
from education.models import Resource


@login_required
def waste_quiz(request):
    """
    Interactive waste management quiz with pagination
    """
    questions = QuizQuestion.objects.all().order_by('?')  # Randomize questions
    paginator = Paginator(questions, 5)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        # Save user answers for current page in session
        user_answers = request.session.get('user_answers', {})

        for question in page_obj.object_list:
            answer = request.POST.get(str(question.id))
            if answer:
                user_answers[str(question.id)] = answer

        request.session['user_answers'] = user_answers

        # Navigate to next page or show results
        if page_number < paginator.num_pages:
            next_page = page_number + 1
            return redirect(f"{request.path}?page={next_page}")
        else:
            # Calculate final score and prepare detailed feedback
            score = 0
            total = questions.count()
            feedback = []

            for question in questions:
                user_answer = user_answers.get(str(question.id))
                is_correct = (
                    user_answer and 
                    user_answer.strip().lower() == question.correct_answer.strip().lower()
                )
                
                if is_correct:
                    score += 1
                    
                feedback.append({
                    "question": question.question,
                    "correct_answer": question.correct_answer,
                    "user_answer": user_answer or "Not answered",
                    "explanation": question.explanation,
                    "is_correct": is_correct
                })

            # Save score to database
            QuizScore.objects.create(user=request.user, score=score)

            # Clear session data
            if 'user_answers' in request.session:
                del request.session['user_answers']

            # Add success message
            percentage = (score / total) * 100
            if percentage >= 80:
                messages.success(request, f"Excellent! You scored {score}/{total} ({percentage:.1f}%)")
            elif percentage >= 60:
                messages.info(request, f"Good job! You scored {score}/{total} ({percentage:.1f}%)")
            else:
                messages.warning(request, f"You scored {score}/{total} ({percentage:.1f}%). Keep learning!")

            return render(request, "educ/quiz_result.html", {
                "score": score,
                "total": total,
                "percentage": percentage,
                "feedback": feedback
            })

    return render(request, "educ/quiz.html", {
        "page_obj": page_obj,
        "current_page": page_number,
        "total_pages": paginator.num_pages,
    })


@login_required
def quiz_leaderboard(request):
    """
    Display quiz scores leaderboard
    """
    top_scores = QuizScore.objects.select_related('user').order_by('-score', 'date')[:10]
    user_scores = QuizScore.objects.filter(user=request.user).order_by('-date')[:5]
    
    return render(request, "educ/leaderboard.html", {
        'top_scores': top_scores,
        'user_scores': user_scores,
    })