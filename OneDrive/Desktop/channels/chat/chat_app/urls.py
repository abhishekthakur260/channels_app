# chat/urls.py
from django.urls import path

from .import views

urlpatterns = [
    path("chat/", views.index, name="index"),
    path("<str:room_name>/", views.chatroom, name="index"),
]