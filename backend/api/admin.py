from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'mobile_no', 'is_active', 'is_staff', 'is_superuser', 'date_joined') #changed staff and admin to is_staff and is_superuser, and added date_joined
    list_filter = ('is_active', 'is_staff', 'is_superuser') #changed staff and admin to is_staff and is_superuser
    search_fields = ('email', 'first_name', 'last_name', 'mobile_no')
    ordering = ('email',)

    filter_horizontal = ('groups', 'user_permissions') #added this line

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'mobile_no')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), #changed staff and admin to is_staff and is_superuser, and added groups and user_permissions
        ('Important dates', {'fields': ('last_login', 'date_joined')}), #changed created_at to last_login and date_joined
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2', 'first_name', 'last_name', 'mobile_no', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), #changed staff and admin to is_staff and is_superuser, and added groups and user_permissions
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.password:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)