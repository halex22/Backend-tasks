from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Message, MessageBoard, MyUser
from .serializers import (MessageBoardSerializer, MessageSerializer,
                          UserSerializer)


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()
        message_board_id = self.request.query_params.get('message_board_id')

        if message_board_id:
            queryset = queryset.filter(message_board_id= message_board_id)
            
        return queryset    


class MessageBoardViewSet(ModelViewSet):
    serializer_class = MessageBoardSerializer
    queryset = MessageBoard.objects.all()


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()