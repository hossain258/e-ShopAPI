from django.contrib import admin
from App_UserProfile.models import UserProfile

# Register your models here.
@admin.register(UserProfile)

class userprofileadmin(admin.ModelAdmin):
    list_display=['username','email','phone']
