from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, QuickRegisterForm,ProfileEditForm
from .models import Profile
from django.views.decorators.csrf import csrf_protect
import logging

logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data['user_type']
            location = form.cleaned_data['location']
            contact = form.cleaned_data['contact']
            accepted_waste_types = ','.join(form.cleaned_data.get('accepted_waste_types', []))
            
            profile = Profile(
                user=user,
                user_type=user_type,
                location=location,
                contact=contact,
                accepted_waste_types=accepted_waste_types
            )
            profile.save()
            
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
        is_quick_access = profile.user_type == 'quick_access'
    except Profile.DoesNotExist:
        profile = None
        is_quick_access = False

    return render(request, 'users/profile.html', {
        'profile': profile,
        'is_quick_access': is_quick_access,
    })


@csrf_protect
def user_login(request):
    """
    Enhanced login view with better error handling and debugging
    """
    try:
        if request.method == 'POST':
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '').strip()
            next_url = request.POST.get('next', request.GET.get('next', 'profile'))

            # Debug logging
            logger.info(f"Login attempt - Username: {username}, Next: {next_url}")

            # Validation
            if not username or not password:
                messages.error(request, 'Username and password are required.')
                return render(request, 'users/login.html', {'next': next_url})

            # Authentication
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    logger.info(f"Successful login for user: {username}")
                    
                    # Check user type and redirect accordingly
                    try:
                        if hasattr(user, 'profile') and user.profile.user_type == 'quick_access':
                            return redirect('quick_dashboard')
                    except Exception as e:
                        logger.warning(f"Profile check failed: {e}")
                        # Continue with normal flow if profile check fails
                    
                    # Safe redirect handling
                    if next_url and next_url != 'None':
                        try:
                            return redirect(next_url)
                        except Exception as e:
                            logger.warning(f"Redirect to {next_url} failed: {e}")
                            return redirect('profile')
                    else:
                        return redirect('profile')
                else:
                    messages.error(request, 'Your account has been disabled.')
                    logger.warning(f"Login attempt for disabled account: {username}")
            else:
                messages.error(request, 'Invalid username or password.')
                logger.warning(f"Failed login attempt for username: {username}")
                
            return render(request, 'users/login.html', {'next': next_url})
        
        # GET request - show login form
        else:
            next_url = request.GET.get('next', 'profile')
            return render(request, 'users/login.html', {'next': next_url})
            
    except Exception as e:
        logger.error(f"Login view error: {str(e)}", exc_info=True)
        messages.error(request, 'An internal error occurred. Please try again.')
        return render(request, 'users/login.html', {'next': request.GET.get('next', 'profile')})
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def quick_register(request):
    if request.method == 'POST':
        form = QuickRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Quick account created!')
            return redirect('quick_dashboard')
    else:
        form = QuickRegisterForm()
    return render(request, 'users/quick_register.html', {'form': form})

@login_required
def quick_dashboard(request):
    try:
        is_quick_access = request.user.profile.user_type == 'quick_access'
    except Profile.DoesNotExist:
        is_quick_access = False
        
    if not is_quick_access:
        return redirect('profile')
        
    return render(request, 'users/quick_dashboard.html', {
        'is_quick_access': is_quick_access,
    })
    
    
    

@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
    
    return render(request, 'users/profile_edit.html', {'form': form})
