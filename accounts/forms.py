from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreateForm(UserCreationForm):
    class meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("main",)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields