from django.contrib import admin
from django.urls import path
# from App_UserProfile.views import User_logout
from django.conf import settings
from django.conf.urls.static import static
from . import views
# Import views 
# from App_UserProfile.views import Home
app_name="App_UserProfile"
urlpatterns = [
    path('sign-up/', views.sign_up, name ='sign_up'),
    # path('logout/', User_logout, name ='User_logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)