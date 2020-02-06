from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ServiceForm, UserUpdateForm, ServiceUpdateForm, CommentForm, CommentUpdateForm
from .models import Services
from django.http import HttpResponse
import users.databaseAssisting as dbFunc


def clients(request, username):
    activation = dbFunc.is_activated(username)
    return HttpResponse(activation)


def clientsm(request, user):
    message = dbFunc.get_message(user)
    return HttpResponse(message)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        service_form = ServiceForm(request.POST)
        comment_form = CommentForm(request.POST)
        if form.is_valid() and service_form.is_valid() and comment_form.is_valid():
            user = form.save()
            service = service_form.save(commit=False)
            c = comment_form.save(commit=False)
            service.user = user
            c.user = user
            username = form.cleaned_data.get('username')
            service.save()
            c.save()

            messages.success(request, f'Your account has created. You can login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        service_form = ServiceForm()
        comment_form = CommentForm()
    return render(request, 'users/register.html', {'form': form, 'service_form': service_form,
                                                   'comment_form': comment_form, 'title': 'SignUp Page'})




@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        comment_form = CommentForm(request.POST)
        if u_form.is_valid() and comment_form.is_valid():
            u = u_form.save()
            c = comment_form.save(commit=False)
            c.user = u
            username = u_form.cleaned_data.get('username')
            u.save()
            c.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('index')
    else:
        u_form = UserUpdateForm(instance=request.user)
        comment_form = CommentUpdateForm(instance=request.user.comment)
    context = {'u_form': u_form,'comment_form': comment_form, 'title': 'Profile Page'}
    return render(request, 'users/profile.html', context)


@login_required
def service(request):
    if request.method == 'POST':
        u_form = ServiceUpdateForm(request.POST, instance=request.user.services)
        if u_form.is_valid():
            u_form.save()
            if u_form.cleaned_data.get('activation') == 1:
                messages.success(request, f'Your account has been blocked')
            else:
                messages.success(request, f'Your account has been unblocked')
            return redirect('index')
    else:
        u_form = ServiceUpdateForm(instance=Services)
    context = {'u_form': u_form, 'title': 'Service Page'}
    return render(request, 'users/service.html', context)


@login_required
def messagesPage(request):
    if request.method == 'POST':
        m_form = CommentUpdateForm(request.POST, instance=request.user.comment)
        if m_form.is_valid():
            m_form.save()
            messages.success(request, f'Your message accepted')
            return redirect('index')
    else:
        m_form = CommentUpdateForm(instance=request.user.comment)
    context = {'m_form': m_form, 'title': 'Message Page'}
    return render(request, 'users/messagesPage.html', context)



