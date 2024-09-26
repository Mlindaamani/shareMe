from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'bio',
                    'phone_number', 'married', 'gender']
    list_filter = ['gender', 'married']
