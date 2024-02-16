from django.urls import path, include
from django.contrib import admin
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', blog_views.home, name='home'),
]
