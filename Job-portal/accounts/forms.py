from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseForm
from .models import CustomUser

class UserForm(BaseForm):
    class Meta(BaseForm.Meta):
        model=CustomUser
        fields=BaseForm.Meta.fields + ('email', 'is_employer', 'is_employee', 'phone_number', 'location')