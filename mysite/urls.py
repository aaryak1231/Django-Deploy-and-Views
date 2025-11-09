from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    # path('views/', views.post_list, name='post_list'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),   # homepage -> blog.urls
]
