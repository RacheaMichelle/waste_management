from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random

class QuizQuestion(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    # Changed all answer fields to support text instead of waste type choices
    question = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=255)  # Increased length for text answers
    wrong_answer_1 = models.CharField(max_length=255)  # Increased length for text answers
    wrong_answer_2 = models.CharField(max_length=255)  # Increased length for text answers
    wrong_answer_3 = models.CharField(max_length=255)  # Increased length for text answers
    explanation = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    points = models.IntegerField(default=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Quiz Question"
        verbose_name_plural = "Quiz Questions"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.question[:50]}..."
    
    def get_shuffled_answers(self):
        """Return all answers in random order"""
        answers = [
            self.correct_answer,
            self.wrong_answer_1,
            self.wrong_answer_2,
            self.wrong_answer_3
        ]
        random.shuffle(answers)
        return answers


class QuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField(default=10)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Quiz Score"
        verbose_name_plural = "Quiz Scores"
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.user.username} - {self.score}/{self.total_questions} - {self.date.strftime('%Y-%m-%d')}"
    
    def percentage(self):
        return (self.score / self.total_questions) * 100