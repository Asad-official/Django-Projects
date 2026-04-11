from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # We exclude 'user' because we will assign it automatically in the view
        fields = ['title', 'description', 'due_date', 'priority', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }