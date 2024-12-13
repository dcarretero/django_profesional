from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

usuarioPersonalizado = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = usuarioPersonalizado
    list_display = ['email','username','is_superuser']
    

admin.site.register(usuarioPersonalizado, CustomUserAdmin)
    


