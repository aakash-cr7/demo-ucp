from django.conf import settings
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import SignUpForm, LoginForm, ForgotPasswordForm, ResetPasswordForm, AddFavTopicForm
from .models import Student, Staff
from .models import CustomUser, Student, Staff

# Create your views here.

@require_GET
def index(request):
    return redirect('login')

@login_required
def home(request):
    context = {
        'f1': AddFavTopicForm(),
    }
    return render(request, 'base/loggedin.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'GET':
        f = LoginForm()
    else:
        f = LoginForm(request.POST)
        if f.is_valid():
            user = f.get_user()
            auth_login(request, user)
            return JsonResponse(data = { 'success' : True })
        else:
            data = { 'error' : True, 'errors' : dict(f.errors.items()) }
            return JsonResponse(status = 404, data = data)
    return render(request, 'auth/login.html', {'form': f})


@require_GET
def logout(request):
    auth_logout(request)
    return redirect('login')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f = SignUpForm()
    else:
        f = SignUpForm(request.POST)
        if f.is_valid():

            '''
                Check if user is STUDENT or STAFF
            '''
            if(request.POST.get('role') == 'STUDENT'):
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password2')
                enrollment_number = request.POST.get('unique_id')
                try:
                    user = Student.objects.create_user(username, email, password, enrollment_number = enrollment_number)
                except:
                    raise Http404
                user.is_active = False
                user.role = 'STUDENT'
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.save()
            elif(request.POST.get('role') == 'STAFF'):
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password2')
                staff_id = request.POST.get('unique_id')
                try:
                    user = Staff.objects.create_user(username, email, password, staff_id = staff_id)
                except:
                    raise Http404
                user.is_active = False
                user.role = 'STAFF'
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.save()
            else:
                raise Http404

            '''
                *Send activation email to the moderator, to approve student/staff.
                 - Send an activation link along with user info, so that moderator could click on the activation link to
                   activate the user account.

                *Send email verification email to user, to verify their email.
            '''
            email_body_context = {
                'username': user.username,
                'firstname': user.first_name,
                'lastname': user.last_name,
                'user_status': 'Student' if user.role == 'STUDENT' else 'Staff',
                'unique_id': user.enrollment_number if user.role == 'STUDENT' else user.staff_id,
                'token': urlsafe_base64_encode(force_bytes(user.username)),
                'uid': user.id,
                'protocol': 'https' if settings.USE_HTTPS else 'http',
                'domain': get_current_site(request).domain,
            }
            # sending email to moderator
            body_mod = loader.render_to_string('auth/signup_email_body_text_to_moderator.html', email_body_context)
            subject = 'User approval request'
            email_message_mod = EmailMultiAlternatives(subject, body_mod, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_MODERATOR_EMAIL])
            email_message_mod.send()

            # sending email to user
            body_user = loader.render_to_string('auth/signup_email_body_text_to_user.html', email_body_context)
            email_message_user = EmailMultiAlternatives('Email Verification', body_user, settings.DEFAULT_FROM_EMAIL, [user.email])
            email_message_user.send()
            # return render(request, 'auth/signup_email_sent.html', {})
            return JsonResponse(data = { 'success' : True })
        else:
            data = { 'error' : True, 'errors' : dict(f.errors.items()) }
            return JsonResponse(status = 404, data = data)
    return render(request, 'auth/signup.html', {'form': f})

@require_GET
def verify_email(request, uid = None, token = None):
    if request.user.is_authenticated():
        return redirect('home')
    user = get_object_or_404(CustomUser, id = uid)
    username_from_token = force_text(urlsafe_base64_decode(token))
    if user.is_email_verified:
        return redirect('login')

    if user.username == username_from_token:
        user.is_email_verified = True
        user.save()
        return render(request, 'auth/verify_email_success.html')
    else:
        return render(request, 'auth/verify_email_failure.html')

@require_http_methods(['GET', 'POST'])
def forgot_password(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f = ForgotPasswordForm()
    if request.method == 'POST':
        f = ForgotPasswordForm(request.POST)
        if f.is_valid():
            user = CustomUser.objects.get(email = f.cleaned_data.get('email'))
            email_body_context = {
                'username': user.username,
                'token': default_token_generator.make_token(user),
                'uid': user.id,
                'protocol': 'https' if settings.USE_HTTPS else 'http',
                'domain': get_current_site(request).domain,
            }
            body = loader.render_to_string('auth/forgot_password_email_body_text.html', email_body_context)
            subject = 'Reset your password'
            email_message = EmailMultiAlternatives(subject, body, settings.DEFAULT_FROM_EMAIL, [user.email])
            email_message.send()
            context = { 'email': user.email }
            return render(request, 'auth/forgot_password_email_sent.html', context)

    context = { 'form': f }
    return render(request, 'auth/forgot_password.html', context)

@require_http_methods(['GET', 'POST'])
def reset_password(request, uid = None, token = None):
    if request.user.is_authenticated():
        return redirect('home')
    try:
        user = CustomUser.objects.get(id = uid)
    except CustomUser.DoesNotExist:
        user = None
    if not user or not default_token_generator.check_token(user, token):
        context = { 'validlink': False }
        return render(request, 'auth/reset_password.html', context)

    if request.method == 'GET':
        f = ResetPasswordForm()
    else:
        f = ResetPasswordForm(request.POST)
        if f.is_valid():
            user.set_password(f.cleaned_data.get('password1'))
            user.save()
            return redirect('login')

    context = { 'validlink': True, 'form': f }
    return render(request, 'auth/reset_password.html', context)
