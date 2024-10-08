from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

from .models import Food, Category, TagPost


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию')

    class Meta:
        model = Food
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', validators=[MinLengthValidator(2)])
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Сообщение', widget=forms.Textarea, validators=[MinLengthValidator(10)])
    captcha = CaptchaField()