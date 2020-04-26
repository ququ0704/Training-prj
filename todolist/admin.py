from django.contrib import admin
from todolist.models import Todolist
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User

'''class CoderInline(admin.StackedInline):
    model = Coder
    can_delete = False
    verbose_name_plural = 'coder'

class  UserAdmin(BaseUserAdmin):
    inlines = (CoderInline,)'''

# Register your models here.

'''class TodolistAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'discription', 'Is_complete']

class UsrAdmin(admin.ModelAdmin):
    list_display = ['username', 'todolist']

admin.site.register(Todolist, TodolistAdmin)
admin.site.register(Usrs, UsrAdmin)'''



admin.site.register(Todolist)




