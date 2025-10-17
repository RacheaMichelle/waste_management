from django.core.management.base import BaseCommand
from educ.models import QuizQuestion
from django.db import models


class Command(BaseCommand):
    help = 'Load comprehensive quiz questions for waste management education'

    def handle(self, *args, **kwargs):
        questions_data = [
            # PLASTIC WASTE - Engaging Questions
            {
                "question": "♻️ What's the most common mistake people make when recycling plastic bottles?",
                "correct_answer": "Leaving caps on bottles",
                "wrong_answer_1": "Washing them too thoroughly",
                "wrong_answer_2": "Sorting by color",
                "wrong_answer_3": "Crushing them flat",
                "explanation": "🎯 Keep caps ON! Modern recycling facilities can process bottles with caps. This prevents caps from getting lost during sorting. Fun fact: It takes about 10 plastic bottles to make enough plastic fiber for a cool new t-shirt!",
                "difficulty": "easy",
                "points": 10
            },
            {
                "question": "🔥 Plastic bags in Uganda: What should you REALLY do with them?",
                "correct_answer": "Reuse them multiple times",
                "wrong_answer_1": "Put in regular recycling bin",
                "wrong_answer_2": "Burn them safely",
                "wrong_answer_3": "Bury in garden",
                "explanation": "🛍️ Plastic bags clog recycling machinery! Best to reuse them or take to specific collection points. In Uganda, many markets have bag collection bins. Every reused bag saves energy!",
                "difficulty": "medium",
                "points": 15
            },
            {
                "question": "🏆 Which plastic type is MOST valuable for recycling in East Africa?",
                "correct_answer": "PET (Type 1 - Water bottles)",
                "wrong_answer_1": "PVC (Type 3 - Pipes)",
                "wrong_answer_2": "PS (Type 6 - Styrofoam)",
                "wrong_answer_3": "Other (Type 7 - Mixed)",
                "explanation": "💎 PET plastic is highly sought after! It can be recycled into new bottles, clothing, and even construction materials. Kampala has several PET recycling initiatives creating jobs!",
                "difficulty": "hard",
                "points": 20
            },

            # PAPER WASTE - Interactive Questions
            {
                "question": "📦 Your pizza box has grease stains. What's the UGANDA solution?",
                "correct_answer": "Compost it or use for mulch",
                "wrong_answer_1": "Recycle with clean paper",
                "wrong_answer_2": "Burn it immediately",
                "wrong_answer_3": "Throw in general waste",
                "explanation": "🌱 Grease prevents paper recycling but makes great compost! In Uganda, you can tear it up for garden mulch or find community composting sites. Food-contaminated paper helps plants grow!",
                "difficulty": "easy",
                "points": 10
            },
            {
                "question": "💼 Office paper recycling: What percentage can be saved compared to new paper?",
                "correct_answer": "60% energy and water savings",
                "wrong_answer_1": "25% energy savings",
                "wrong_answer_2": "90% cost reduction",
                "wrong_answer_3": "No significant savings",
                "explanation": "💪 Recycling paper saves 60% energy and water! In Uganda, paper recycling creates local jobs and reduces pressure on forests. Every ton of recycled paper saves 17 trees!",
                "difficulty": "medium",
                "points": 15
            },

            # GLASS WASTE - Uganda Context
            {
                "question": "🍶 Broken glass in Uganda: What's the SAFEST disposal method?",
                "correct_answer": "Wrap in paper and label 'broken glass'",
                "wrong_answer_1": "Mix with other recyclables",
                "wrong_answer_2": "Bury in backyard",
                "wrong_answer_3": "Throw in regular bin",
                "explanation": "⚠️ Safety first! Wrap broken glass to protect waste handlers. While Uganda's glass recycling is growing, safety is key. Some artisans actually create beautiful art from broken glass!",
                "difficulty": "easy",
                "points": 10
            },
            {
                "question": "🔄 How many times can glass be recycled without losing quality?",
                "correct_answer": "Infinite times!",
                "wrong_answer_1": "5-10 times",
                "wrong_answer_2": "Only once",
                "wrong_answer_3": "25 times maximum",
                "explanation": "∞ Glass is the recycling champion! It can be recycled forever without quality loss. In Uganda, glass bottles are often returned for refilling - the original recycling!",
                "difficulty": "medium",
                "points": 15
            },

            # ORGANIC WASTE - Local Solutions
            {
                "question": "🍌 What Ugandan kitchen waste makes the BEST compost?",
                "correct_answer": "Banana peels and coffee grounds",
                "wrong_answer_1": "Meat and fish scraps",
                "wrong_answer_2": "Dairy products",
                "wrong_answer_3": "Oily foods",
                "explanation": "🌿 Banana peels are compost gold! They break down quickly and add potassium. Mixed with Ugandan coffee grounds, they create nutrient-rich compost perfect for local gardens!",
                "difficulty": "easy",
                "points": 10
            },
            {
                "question": "🐔 In Ugandan homes, what's a traditional way to handle food scraps?",
                "correct_answer": "Feed to chickens or livestock",
                "wrong_answer_1": "Burn in backyard",
                "wrong_answer_2": "Flush down toilet",
                "wrong_answer_3": "Bury in plastic bags",
                "explanation": "🐓 Traditional wisdom! Feeding scraps to animals reduces waste and provides free feed. Many Ugandan households keep chickens that happily eat vegetable peels and leftovers.",
                "difficulty": "easy",
                "points": 10
            },

            # E-WASTE - Critical for Uganda
            {
                "question": "📱 Your old phone in Uganda: Where should it go?",
                "correct_answer": "E-waste collection point",
                "wrong_answer_1": "Regular garbage bin",
                "wrong_answer_2": "Burn for metal recovery",
                "wrong_answer_3": "Bury in compound",
                "explanation": "🔋 E-waste contains valuable metals AND toxic materials! Uganda has growing e-waste collection points. Your old phone might help someone get connected or provide materials for new devices!",
                "difficulty": "medium",
                "points": 15
            },
            {
                "question": "💡 What valuable metal in phones is worth more than gold?",
                "correct_answer": "Palladium",
                "wrong_answer_1": "Copper",
                "wrong_answer_2": "Aluminum",
                "wrong_answer_3": "Tin",
                "explanation": "💰 Palladium is super valuable! Recycling phones recovers precious metals. In Uganda, proper e-waste recycling can create jobs and reduce environmental pollution from mining.",
                "difficulty": "hard",
                "points": 20
            },

            # METAL WASTE - Local Context
            {
                "question": "🥫 In Uganda, what happens to most metal cans?",
                "correct_answer": "Informal sector recycling",
                "wrong_answer_1": "Landfill disposal",
                "wrong_answer_2": "Export for recycling",
                "wrong_answer_3": "Ocean dumping",
                "explanation": "🔧 Uganda has a vibrant informal recycling sector! Metal collectors often buy cans and scrap, supporting local economies. This traditional system helps keep metals in use.",
                "difficulty": "easy",
                "points": 10
            },

            # CLOTHING - Uganda Specific
            {
                "question": "👕 What's the best fate for old clothes in Uganda?",
                "correct_answer": "Donate or repurpose locally",
                "wrong_answer_1": "Burn for quick disposal",
                "wrong_answer_2": "Export overseas",
                "wrong_answer_3": "Landfill burial",
                "explanation": "🤝 Donating clothes supports communities! Many organizations in Uganda redistribute quality used clothing. Damaged clothes can become cleaning rags or be transformed by local tailors.",
                "difficulty": "easy",
                "points": 10
            },

            # CONSTRUCTION WASTE
            {
                "question": "🏗️ In Ugandan construction, what waste is most valuable to reuse?",
                "correct_answer": "Bricks and concrete",
                "wrong_answer_1": "Plastic packaging",
                "wrong_answer_2": "Wood scraps",
                "wrong_answer_3": "Metal cuttings",
                "explanation": "🧱 Bricks and concrete can be crushed for new construction! This saves money and reduces quarrying. Many Ugandan builders reuse materials creatively.",
                "difficulty": "medium",
                "points": 15
            },

            # SPECIAL CHALLENGE QUESTIONS
            {
                "question": "🎯 UGANDA CHALLENGE: Which waste stream is growing fastest in Kampala?",
                "correct_answer": "Plastic packaging",
                "wrong_answer_1": "Food waste",
                "wrong_answer_2": "Construction debris",
                "wrong_answer_3": "Medical waste",
                "explanation": "📈 Plastic packaging is exploding! But this means recycling opportunities are growing too. Many Ugandan entrepreneurs are creating businesses from plastic waste.",
                "difficulty": "hard",
                "points": 25
            },
            {
                "question": "🌟 BONUS: What percentage of Uganda's waste could be composted?",
                "correct_answer": "Over 60%",
                "wrong_answer_1": "About 25%",
                "wrong_answer_2": "Less than 10%",
                "wrong_answer_3": "Exactly 45%",
                "explanation": "🌍 Over 60% of Uganda's waste is organic! Composting could transform our waste management and create rich soil for agriculture. Every household can contribute!",
                "difficulty": "hard",
                "points": 25
            }
        ]

        created_count = 0
        updated_count = 0

        for i, data in enumerate(questions_data, 1):
            # Check if question already exists
            existing_question = QuizQuestion.objects.filter(question=data["question"]).first()
            
            if existing_question:
                # Update existing question
                for field, value in data.items():
                    setattr(existing_question, field, value)
                existing_question.save()
                updated_count += 1
                self.stdout.write(f"🔄 Updated {i:2d}: {data['question'][:50]}...")
            else:
                # Create new question
                QuizQuestion.objects.create(**data)
                created_count += 1
                self.stdout.write(f"✅ Created {i:2d}: {data['question'][:50]}...")

        total_questions = QuizQuestion.objects.count()
        
        self.stdout.write("\n" + "="*70)
        self.stdout.write(
            self.style.SUCCESS(
                f'🎉 QUIZ LOADING COMPLETE!\n'
                f'📊 Questions Created: {created_count}\n'
                f'🔄 Questions Updated: {updated_count}\n'
                f'📚 Total Questions in Database: {total_questions}\n'
                f'🏆 Difficulty Levels: Easy, Medium, Hard\n'
                f'⭐ Point System: 10-25 points per question'
            )
        )
        self.stdout.write("="*70)

        # Show breakdown by difficulty
        self.stdout.write("\n📊 BREAKDOWN BY DIFFICULTY:")
        self.stdout.write("-" * 40)
        difficulties = ['easy', 'medium', 'hard']
        for diff in difficulties:
            count = QuizQuestion.objects.filter(difficulty=diff).count()
            points_sum = QuizQuestion.objects.filter(difficulty=diff).aggregate(total_points=models.Sum('points'))['total_points'] or 0
            self.stdout.write(f"  {diff.upper():8} : {count:2d} questions ({points_sum} total points)")

        total_points_available = QuizQuestion.objects.aggregate(total=models.Sum('points'))['total'] or 0
        self.stdout.write(f"\n🌟 TOTAL POINTS AVAILABLE: {total_points_available}")

        # Show some fun statistics
        self.stdout.write("\n🎯 FUN STATS:")
        self.stdout.write("-" * 40)
        self.stdout.write(f"📝 Average points per question: {total_points_available/total_questions:.1f}")
        
        # Count questions by waste type (approximate based on content)
        plastic_questions = QuizQuestion.objects.filter(question__icontains='plastic').count()
        paper_questions = QuizQuestion.objects.filter(question__icontains='paper').count()
        glass_questions = QuizQuestion.objects.filter(question__icontains='glass').count()
        organic_questions = QuizQuestion.objects.filter(question__icontains='compost').count() + QuizQuestion.objects.filter(question__icontains='food').count()
        
        self.stdout.write(f"♻️ Plastic questions: {plastic_questions}")
        self.stdout.write(f"📚 Paper questions: {paper_questions}")
        self.stdout.write(f"🍶 Glass questions: {glass_questions}")
        self.stdout.write(f"🌿 Organic waste questions: {organic_questions}")
        self.stdout.write(f"📱 E-waste questions: {QuizQuestion.objects.filter(question__icontains='phone').count()}")