from django.urls import path, include
from django.contrib import admin
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', account_views.home, name='home'),  # home view accessible directly from '/'
]
