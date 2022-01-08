from django.urls import path
from .views import ChannelView, CreateChannelView

urlpatterns = [
    path('channel', ChannelView.as_view()),
    path('create-channel', CreateChannelView.as_view())
]
