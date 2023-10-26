from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, \
    UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def user_login(request):
    """Authorizes a valid user or not."""
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                            username=cd['username'],
                            password=cd['password'])
            if not user:
                return HttpResponse('Invalid login')
            else:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
    context= {
        'form': form
    }
    return render(request, 'account/login.html', context)

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html')

def register(request):
    if request.method != 'POST':
        user_form = UserRegistrationForm()
    else:
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but a void saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            context = {
                'new_user': new_user
            }
            return render(request, "account/register_done.html", context)
    
    context = {
        'user_form': user_form
    }
    return render(request, "account/register.html", context)

@login_required
def edit(request):
    """Enables user to edit profile."""
    if request.method != 'POST':
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    else:
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm( request.POST, instance=request.user.profile,
                                files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating your profile")

    context = {
            'user_form': user_form,
            'profile_form': profile_form
            }
    return render(request,'account/edit.html', context)


@login_required
def settings(request):
    """Application settings handled here"""
    return render(request, "account/settings.html")

@login_required
def delete_account(request):
    """Deletes user account."""
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect("written_app:index")
      
    return render(request, "account/delete_account.html")