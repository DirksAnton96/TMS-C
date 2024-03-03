from django.urls import path, include
from rest_framework import routers
from . import views


app_name="users"

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('users/', views.UserViewSet.as_view(), name="users-list"),
]

