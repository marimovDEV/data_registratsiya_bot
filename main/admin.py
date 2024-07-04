from django.contrib import admin
from .models import Lessons,New_Lessons,Now_Lessons,Students,Users,Hendlers,Bot_admin

from django.contrib.auth.models import User, Group
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'home_address', 'kurs', 'created_at')
    search_fields = ('full_name', 'phone_number', 'kurs')
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'photo')
    search_fields = ('lesson',)
class New_LessonsAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'photo')
    search_fields = ('lesson',)
class Now_LessonsAdmin(admin.ModelAdmin):
   list_display = ('lesson', 'photo')
   search_fields = ('lesson',)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'telegram_id', 'username')
    search_fields = ('full_name', 'telegram_id', 'username')
class BotAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'telegram_id', 'username')
    search_fields = ('full_name', 'telegram_id', 'username')

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Lessons,LessonsAdmin)
admin.site.register(New_Lessons,New_LessonsAdmin)
admin.site.register(Now_Lessons,Now_LessonsAdmin)
admin.site.register(Students,StudentAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(Bot_admin,UsersAdmin)
admin.site.register(Hendlers)