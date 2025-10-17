from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@csrf_exempt
@require_POST
def chatbot_api(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').lower()
        
        # Enhanced response logic
        if any(word in user_message for word in ['thank', 'thanks', 'appreciate']):
            response = "🌟 You're welcome! I'm happy to help with your waste management needs. Is there anything else you'd like to know about Clean Uganda?"
        
        elif any(word in user_message for word in ['sign up', 'signup', 'register', 'create account', 'new account']):
            response = "📝 To sign up for Clean Uganda:\n\n1. Click 'Login' in the top navigation\n2. Select 'Register' or 'Sign Up'\n3. Fill in your details:\n   - Full name\n   - Email address\n   - Choose user type (Household, Business, or Collector/Recycler)\n   - Create a secure password\n4. Verify your email (if required)\n5. Complete your profile with location details\n\n💡 Pro tip: Choose the correct user type as it determines what features you can access!"
        
        elif any(word in user_message for word in ['log in', 'login', 'sign in', 'access account']):
            response = "🔐 To log in to Clean Uganda:\n\n1. Click 'Login' in the top navigation\n2. Enter your email and password\n3. Click 'Login' to access your dashboard\n\n🔒 Forgot password? Click 'Forgot Password' to reset it via email.\n\nOnce logged in, you can:\n- Create waste listings\n- View matches\n- Access educational resources\n- Take quizzes\n- Report illegal dumping"
        
        elif 'report' in user_message or 'dumping' in user_message:
            response = "🚨 To report illegal dumping:\n\n1. Go to 'Report Dumping' page\n2. Click on the map to select location\n3. Add description of the dumping\n4. Upload photos as evidence\n5. Submit the report\n\n📱 No account needed! Authorities will be notified immediately and take action."
        
        elif 'match' in user_message or 'connect' in user_message:
            response = "🤝 How matching works:\n\nFOR WASTE GENERATORS (Households/Businesses):\n1. Create waste listings with type, quantity, location\n2. Our system automatically matches you with nearby collectors\n3. Check 'Matches' page to see interested collectors\n4. Communicate and arrange pickup\n\nFOR COLLECTORS/RECYCLERS:\n1. Set up your profile with accepted waste types\n2. Browse available listings in your area\n3. Send match requests to generators\n4. Coordinate pickup and recycling"
        
        elif 'waste type' in user_message or 'list' in user_message or 'create listing' in user_message:
            response = "🗑️ Creating Waste Listings:\n\n1. Go to 'List Waste' in the menu\n2. Select waste type: Plastic, Paper, Glass, Organic, Metal, E-waste, Clothing, Hazardous, Construction, or Medical\n3. Specify quantity and unit (kg, liters, pieces)\n4. Add your location\n5. Include description and photos\n6. Set status (Available, Pending, Collected)\n\n💡 Be specific about quantity and condition for better matches!"
        
        elif 'recycle' in user_message and 'plastic' in user_message:
            response = "♻️ Plastic Recycling Guide:\n\n1. COLLECTION: Gather plastic waste\n2. SORTING: Separate by type (PET#1, HDPE#2, etc.)\n3. CLEANING: Wash thoroughly, remove labels\n4. PREPARATION: Remove caps and non-plastic parts\n\n🔄 Recycled plastic becomes:\n- New bottles and containers\n- Furniture and construction materials\n- Clothing and textiles\n- Ugandan crafts and products\n\n📚 Check 'Educational Resources' for detailed guides!"
        
        elif 'collector' in user_message or 'recycler' in user_message:
            response = "👷 For Collectors/Recyclers:\n\nSETUP:\n1. Register as 'Collector/Recycler' user type\n2. Complete your profile with:\n   - Business name and contact\n   - Waste types you accept\n   - Service areas/locations\n   - Processing capabilities\n\nOPERATION:\n1. Browse available waste listings\n2. Send match requests to generators\n3. Coordinate pickup logistics\n4. Update listing status after collection\n5. Provide recycling documentation\n\n💼 Regular profile updates increase your visibility!"
        
        elif 'household' in user_message or 'business' in user_message:
            response = "🏠 For Households & Businesses:\n\nGETTING STARTED:\n1. Register as 'Household' or 'Business'\n2. Set your location for local matches\n3. Start listing your waste materials\n\nBENEFITS:\n- Connect with verified collectors\n- Learn proper waste management\n- Report environmental issues\n- Access educational resources\n- Earn recognition for eco-friendly practices"
        
        elif any(word in user_message for word in ['quiz', 'quizzes', 'test', 'learn', 'education']):
            response = "🎯 Waste Management Quizzes:\n\nAVAILABLE QUIZZES:\n• Plastic Recycling Knowledge\n• Paper & Cardboard Recycling\n• Glass Waste Management\n• Organic Waste Composting\n• E-Waste Handling\n• Metal Recycling\n• General Waste Segregation\n\n📊 FEATURES:\n- Multiple difficulty levels (Easy, Medium, Hard)\n- Points system for correct answers\n- Detailed explanations for learning\n- Progress tracking\n- Uganda-specific content\n\n🚀 Access: Go to 'Waste Quiz' in the main menu to test your knowledge!"
        
        elif 'location' in user_message or 'area' in user_message:
            response = "📍 Location Services:\n\nWHY LOCATION MATTERS:\n• Connects you with nearby users\n• Enables local waste collection\n• Helps in reporting dumping sites\n• Provides relevant recycling info\n\nSETTING LOCATION:\n1. Go to your Profile\n2. Click 'Edit Profile'\n3. Enter your address or use map\n4. Save changes\n\n🔒 Your exact location is never shared publicly - only general area for matching."
        
        elif any(word in user_message for word in ['help', 'support', 'problem', 'issue']):
            response = "💡 How can I help you?\n\nI can assist with:\n\n🔸 ACCOUNT: Sign up, Login, Profile setup\n🔸 WASTE LISTINGS: Creating, editing, managing\n🔸 MATCHING: How it works, finding partners\n🔸 RECYCLING: Processes for different materials\n🔸 REPORTING: Illegal dumping procedures\n🔸 EDUCATION: Quizzes and learning resources\n🔸 NAVIGATION: Using the platform features\n\nWhat specific help do you need today?"
        
        elif any(word in user_message for word in ['hello', 'hi', 'hey', 'greetings']):
            response = "👋 Hello! I'm CleanBot, your waste management assistant for Clean Uganda! 🌍\n\nI can help you with:\n• Account setup and login\n• Waste listing creation\n• Recycling information\n• Matching with collectors\n• Reporting illegal dumping\n• Educational quizzes\n• Platform navigation\n\nWhat would you like to know about our waste management platform?"
        
        elif any(word in user_message for word in ['feature', 'what can', 'capabilities']):
            response = "🚀 Clean Uganda Platform Features:\n\n📋 WASTE LISTINGS:\n- Create and manage waste listings\n- Specify type, quantity, location\n- Upload photos\n\n🤝 SMART MATCHING:\n- Automatic matching with local collectors\n- Real-time notifications\n- Communication tools\n\n📚 EDUCATION:\n- Interactive quizzes\n- Recycling guides\n- Uganda-specific resources\n\n🚨 REPORTING:\n- Illegal dumping reports\n- Photo evidence upload\n- Authority notifications\n\n📊 ANALYTICS:\n- Waste tracking\n- Recycling impact\n- Personal statistics\n\nWhich feature would you like to explore?"
        
        elif any(word in user_message for word in ['uganda', 'kampala', 'ugandan']):
            response = "🇺🇬 Clean Uganda - Local Focus:\n\nSPECIFIC TO UGANDA:\n• Local recycling facilities information\n• Uganda waste management regulations\n• Kampala-specific collection points\n• Ugandan success stories\n• Local language support\n• Community-based initiatives\n\n🌱 We work with:\n- Local authorities\n- Community organizations\n- Ugandan recyclers\n- Environmental agencies\n\nTogether, we're making Uganda cleaner!"
        
        else:
            response = "🤖 I'm here to help you with Clean Uganda's waste management platform!\n\nYou can ask me about:\n\n🔐 ACCOUNT: 'How do I sign up?' or 'Login help'\n🗑️ WASTE: 'How to create a listing?'\n🤝 MATCHING: 'How does matching work?'\n📚 LEARNING: 'Tell me about quizzes'\n🚨 REPORTING: 'How to report dumping?'\n📍 LOCATION: 'Setting my area'\n\nOr type 'features' to see all platform capabilities!\n\nWhat would you like to know?"
            
        return JsonResponse({'response': response})
        
    except Exception as e:
        return JsonResponse({'response': 'Sorry, I encountered an error. Please try again or refresh the page.'})

def chatbot_demo(request):
    """Simple demo page for chatbot"""
    return JsonResponse({'message': 'CleanBot API is working! Ready to assist with waste management in Uganda.'})