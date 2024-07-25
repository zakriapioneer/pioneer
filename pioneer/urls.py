# pioneer/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('signup.urls')),  # Include the signup app's URLs
    # path('', include('django.contrib.auth.urls')),  # Built-in auth views for login/logout
]
