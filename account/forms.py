from django import forms
from django.contrib.auth import authenticate
from material import Layout, Span6, Row
from .models import CustomUser, Student, Staff

ROLE_CHOICES =  (
    ('STAFF', 'staff'),
    ('STUDENT', 'stud'),
)

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 100, widget = forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        data_username = self.cleaned_data.get('username')
        data_password = self.cleaned_data.get('password')

        if data_username and data_password:
            if len(data_username) < 6:
                raise forms.ValidationError('username is too short (minimum is 6 characters) ')
            self.user_cache = authenticate(username = data_username, password = data_password)

            if self.user_cache is None:
                raise forms.ValidationError('Invalid username or password')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('User is not yet approved by the moderator/admin')
            elif not self.user_cache.is_email_verified:
                raise forms.ValidationError('User email not yet verified')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    username = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 50)
    unique_id = forms.IntegerField(label = 'Enrollment number/staff id',help_text = 'please write your unique roll number/staff id')
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput, help_text = 'should be same as Password')
    role = forms.ChoiceField(label='select an option', choices=ROLE_CHOICES, widget=forms.RadioSelect)
    layout = Layout(
        Row(Span6('first_name'), Span6('last_name')),
        Row('username'),
        Row('email'),
        Row('unique_id'),
        Row('password1'),
        Row('password2'),
        Row('role'),
    )
    '''
        username should be min 6 characters
    '''
    def clean_username(self):
        data_username = self.cleaned_data.get('username')

        if data_username and CustomUser.objects.filter(username = data_username).count() != 0:
            raise forms.ValidationError('username already exists')
        if len(data_username) < 6:
            raise forms.ValidationError('username is too short (minimum is 6 characters) ')
        return data_username

    '''
        password should be min 6 characters
    '''
    def clean_password2(self):
        data_password1 = self.cleaned_data.get('password1')
        data_password2 = self.cleaned_data.get('password2')

        if data_password1 and data_password2 and data_password1 != data_password2:
            raise forms.ValidationError('Passwords don\'t match')
        if len(data_password2) < 6:
            raise forms.ValidationError('Password is too short (minimum is 6 characters) ')
        return data_password2

    '''
        Checking if enrollment number/staff id exists already
    '''
    def clean_unique_id(self):
        data_unique_id = self.cleaned_data.get('unique_id')
        if data_unique_id and Student.objects.filter(enrollment_number = data_unique_id).count() != 0 or Staff.objects.filter(staff_id = data_unique_id).count() != 0:
            raise forms.ValidationError('enrollment number/ staff id already exist')

    '''
        Checking if email exists already
    '''
    def clean_email(self):
        data_email = self.cleaned_data.get('email')
        if data_email and CustomUser.objects.filter(email = data_email).count() != 0:
            raise forms.ValidationError('email already exists')
        '''
            Further check if the username has the college domain, name etc. goes here
            ......
            ....
        '''
        return data_email

class ForgotPasswordForm(forms.Form):
   email = forms.EmailField(max_length = 254)

   def clean_email(self):
       data_email = self.cleaned_data.get('email')
       if data_email and CustomUser.objects.filter(email = data_email).count() == 0:
           raise forms.ValidationError('Can\'t find that email, sorry')
       return data_email

class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput, help_text = 'Should be same as Password')

    def clean_password2(self):
        data_password1 = self.cleaned_data.get('password1')
        data_password2 = self.cleaned_data.get('password2')

        if data_password1 and data_password2 and data_password1 != data_password2:
            raise forms.ValidationError('Passwords don\'t match')
        if len(data_password2) < 6:
            raise forms.ValidationError('Password is too short (minimum is 6 characters) ')
        return data_password2

class AddFavTopicForm(forms.Form):
    name = forms.CharField(label = 'Topics', max_length = 100)
