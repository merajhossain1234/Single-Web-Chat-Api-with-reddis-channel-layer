from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



from .tokenauthentication import JWTAuthentication  # Import your JWTAuthentication class



class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)




