from django.contrib.auth import forms

from .models import User


class UserChangeForm(forms.UserChangeForm): # Extendedo a classe
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User