from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):

    def __str__(self):
        return f'{self.username}'


class MessageBoard(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(MyUser, related_name='message_board', blank=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'message_boards'
    

class Message(models.Model):
    message_board = models.ForeignKey(MessageBoard, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='messages')
    body = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = 'messages'
        get_latest_by = 'created'
        ordering = ['-created']
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return f'{self.author.username}: {self.body[:50]}'