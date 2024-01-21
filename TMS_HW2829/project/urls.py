"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import serve

from posts.views import home_page_view, create_note_view, show_note_view, show_about_view, update_note_view, delete_node,register,user_notes,profile_update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/register', register, name="register"),
    
    
    path("", home_page_view, name="home"),
    path("create", create_note_view, name="create-note"),
    path("post/<note_uuid>", show_note_view, name="show-note"),
    path("show-about", show_about_view, name="show-about"),
    path("edit/<note_uuid>", update_note_view, name="update-note"),
    path("delete/<note_uuid>", delete_node, name="delete-node"),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path("user/<username>/notes", user_notes, name="user_notes"),
    path("profile/<username>", profile_update_view, name="profile-view"),
    
    path('api/posts/',include('posts.api.urls')),
]
