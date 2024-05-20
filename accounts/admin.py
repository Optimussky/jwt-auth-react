from django.contrib import admin
#from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomAdminUser(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser