from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, QuickRegisterForm,ProfileEditForm
from .models import Profile


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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'users/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    if user.profile.user_type == 'quick_access':
                        return redirect('quick_dashboard')
                except Profile.DoesNotExist:
                    pass

                next_url = request.GET.get('next', 'profile')
                return redirect(next_url)
            else:
                messages.error(request, 'Account is disabled.')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')

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