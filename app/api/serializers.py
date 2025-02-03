from typing import Type

from rest_framework.serializers import (CharField, ModelSerializer,
                                        PrimaryKeyRelatedField,
                                        StringRelatedField)

from .models import Message, MessageBoard, MyUser


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True, style={'input_type':'password'})

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']

    
    def create(self, validated_data):
        user = MyUser.objects.create_user(
            username= validated_data['username'],
            email=validated_data.get('email', ''),
            password= validated_data['password']
        )
        return user
    

class MessageBoardSerializer(ModelSerializer):
    author = StringRelatedField()

    class Meta:
        model = Message
        fields = '__all__'


class MessageBoardSerializer(ModelSerializer):
    subscribers = StringRelatedField(many=True, read_only=True)

    class Meta:
        model = MessageBoard
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance: Type[MessageBoard], validated_data):
        new_subscriber = validated_data.get('subscriber')
        instance.subscribers.add(new_subscriber)
        return instance
    

class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'