from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile

# 1. Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'accounts/register.html', {'form': form})


# 2. Profile View (With Auto Profile Check & Edit Forms)
@login_required
def profile(request):
    # Safety Check: Agar user ki profile missing ho toh auto-create karega
    profile_obj, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Aapki profile successfully update ho gayi hai!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    all_users = None
    if request.user.is_superuser:
        all_users = User.objects.all()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'all_users': all_users
    }

    return render(request, 'accounts/profile.html', context)