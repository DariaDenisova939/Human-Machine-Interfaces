from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from main.models import Authors, Courses, Timetable, UsersCourses, Complaints, Applications
from django.forms import ModelForm, TextInput


class AuthorsForm(ModelForm):
    class Meta:
        model = Authors
        fields = ['id_user', 'name', 'surname', 'patronymic']
        widgets = {
            "id_user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id пользователя'}),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'}),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'}),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'}),
        }


class TimetableForm(ModelForm):
    class Meta:
        model = Timetable
        fields = ['start_date', 'end_date', 'name', 'id_user']
        widgets = {
            "start_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата начала прохождения курса'}),
            "end_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания прохождения курса'}),
            "id_user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id пользователя'}),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'}),
        }


class ApplicationForm(ModelForm):
    purpose = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Цель'}))

    class Meta:
        model = Applications
        fields = ['id_user', 'name', 'surname', 'patronymic', 'purpose']
        widgets = {
            "id_user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id пользователя'}),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'}),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'}),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'}),
            "purpose": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Причина'}),
        }


class ComplaintsForm(ModelForm):
    complaint = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Жалоба'}))

    class Meta:
        model = Complaints
        fields = ['complaint', 'id_course']
        widgets = {
            "complaint": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жалоба'}),
            "id_course": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id курса'}),
        }


class CourseForm(ModelForm):
    header = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Заголовок курса'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание курса'}))
    main_text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Тело курса'}))

    class Meta:
        model = Courses
        fields = ['header', 'description', 'main_text', 'name', 'id_author']
        widgets = {
            "header": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок курса'}),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание курса'}),
            "main_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тело курса'}),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'}),
            "id_author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id Автора'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "password1": forms.PasswordInput(attrs={'class': 'form-control'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'size': '4vw'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'size': '5vw'}))
