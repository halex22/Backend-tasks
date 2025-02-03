from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MessageBoardViewSet, MessageViewSet, UsersViewSet

api_router = DefaultRouter()
api_router.register(r'messages', MessageViewSet, basename='messages')
api_router.register(r'message-boards', MessageBoardViewSet, basename='message_boards')
api_router.register(r'users', UsersViewSet, basename='users')


urlpatterns = [
    path('v1/', include((api_router.urls, 'v1')))
]


