from django.contrib import admin
from django.urls import path
from App_UserProfile.views import User_logout
from django.conf import settings
from django.conf.urls.static import static
# Import views 
# from App_UserProfile.views import Home
app_name="App_UserProfile"
urlpatterns = [
    path('logout/', User_logout, name ='User_logout'),
    
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)