from django.shortcuts import render
from rest_framework import generics
from .models import Message,Room,User
from .serializers import MessageSerializer,RoomSerializer,Userserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
import json

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    ordering = ('-timestamp',)
    
    def get_queryset(self):
        room_name = self.kwargs.get('room_name')
        if room_name:
            queryset = Message.objects.filter(room__name=room_name)
        else:
            queryset = Message.objects.all()
        return queryset

class Chatroomlist(generics.ListCreateAPIView):
    serializer_class = RoomSerializer

    def post(self, request):
        username = request.data.get('username')
        print(username)
        user = User.objects.get(username=username)
        
        # Check if user exists before proceeding
        if user is not None:
            queryset = Room.objects.filter(userslist__in=[user.id])
            serializer = RoomSerializer(queryset, many=True)
            userslist = [user_id for room in serializer.data for user_id in room['userslist']]
            users = []
            userslist_values = list(set(userslist))
            for x in userslist_values:
                if x != user.id:
                    userr = User.objects.get(id=x)
                    serializer = Userserializer(userr)
                    users.append(serializer.data)
                    print(serializer.data)
            return Response(data=users, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
         