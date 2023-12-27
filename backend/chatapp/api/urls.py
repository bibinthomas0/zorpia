from django.urls import path

from . import views



urlpatterns = [
    path('chat/<slug:room_name>/messages/', views.MessageList.as_view(), name='chat-messages'),
    path('chatrooms/', views.Chatroomlist.as_view(), name='chatrooms'),
]