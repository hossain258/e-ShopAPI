
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("App_shop.urls")),
    path("", include("App_store.urls")),
    path("user/", include("App_UserProfile.urls")),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    
    # authontication route
    path('', include('django.contrib.auth.urls')),
]
