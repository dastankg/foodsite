from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-input'}))

    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-input'}))

    password1 = forms.CharField(label='Password', max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    password2 = forms.CharField(label='Repeat password', max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First name',
            'last_name': 'Last name',
            'password1': 'Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exists')
        return email


#  Объявите класс формы LectorRegisterForm на базе класса UserCreationForm со следующими элементами:
#
# через атрибуты класса:
#
# username: текстовое поле, максимальная длина 50 символов, название "Логин", CSS-стили attrs={'class': 'form-input'};
# password1: поле ввода пароля, максимальная длина 30 символов, название "Пароль", CSS-стили attrs={'class': 'form-input'};
# password2: поле ввода пароля, максимальная длина 30 символов, название "Повтор пароля", CSS-стили attrs={'class': 'form-input'};
# через атрибуты вложенного класса Meta:
#
# модель: определяется вызовом функции get_user_model();
# отображаемые в форме поля: username, first_name, last_name, email, password1, password2;
# дополнительные метки (названия) полей: first_name -> "Имя", last_name -> "Фамилия", email -> "E-mail".

class LectorRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-input'}))

    password1 = forms.CharField(label='Пароль', max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    password2 = forms.CharField(label='Повтор пароля', max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'E-mail',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exists')
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    this_year = datetime.now().year
    data_of_birth = forms.DateField(label='Дата рождения',
                                    widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 5))))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'photo']
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'E-mail',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', max_length=100,
                                   widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    new_password1 = forms.CharField(label='Новый пароль', max_length=100,
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    new_password2 = forms.CharField(label='Повторите новый пароль', max_length=100,
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))


