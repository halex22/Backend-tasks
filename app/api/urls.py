from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MessageViewSet

api_router = DefaultRouter()
api_router.register(r'messages', MessageViewSet, basename='messages')


urlpatterns = [
    path('v1/', include((api_router.urls, 'v1')))
]


