from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Message, MessageBoard, MyUser
from .serializers import (MessageBoardSerializer, MessageSerializer,
                          UserSerializer)


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
