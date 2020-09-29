from django.contrib import admin
from .models import User, Task

# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task
    extra = 3

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User",{'fields': ['user','gender']}),
    ]
    inlines = [TaskInline]
    list_display = ('user', 'gender','pub_date')

admin.site.register(User, UserAdmin)
