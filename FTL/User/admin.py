from django.contrib import admin
from User.models import CustomUser,UserActivity

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserActivity)
