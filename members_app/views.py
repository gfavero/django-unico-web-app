import email
import imp
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .forms import RegisterUserForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .forms import UserUpdateForm, ProfileUpdateForm,ProfileUpdateForm_edit

@login_required
@staff_member_required
def user_list(request):
    all_users = User.objects.all()
    context = {'all_users':all_users}
    return render(request, 'auth/user_list.html', context)

@login_required
def profile_edit(request,user_local):
    user_edit = User.objects.get(pk=user_local)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user_edit)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=user_edit.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Perfil updated!')
            return redirect('user-list')
    else:
        u_form = UserUpdateForm(instance=user_edit)
        p_form = ProfileUpdateForm(instance=user_edit.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_edit' : user_edit
    }
    return render(request, 'auth/profile.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm_edit(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Perfil updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm_edit(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_edit' : request.user
    }
    return render(request, 'auth/profile.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Você esta logado " + username + "!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error!"))
            return redirect('login')
    else:
        return render(request, 'auth/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Você saiu do ContentLab. Quer entrar novamente?"))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Cadastro completo!"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'auth/register_user.html', {'form': form})

#https://www.youtube.com/watch?v=0pa75ch0S4E
# def PasswordResetView(request):
#     if request.method == "POST":
#         form = PasswordResetForm(request.POST)
#         data = form.cleaned_data.get('email')
#         user_email = User.objects.filter(Q(email=data))
#         if user_email.exists():
#             for user in user_email:
#                 subject = "Password Request"
#     else:
#         form = PasswordResetForm()

#     return render(request, 'auth/password_reset.html', {'form': form})

