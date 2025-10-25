from django.contrib import admin
from .models import Users

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", )
  
admin.site.register(Users, MemberAdmin)