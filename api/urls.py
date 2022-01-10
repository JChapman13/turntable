from django.urls import path
from .views import ChannelView, CreateChannelView, GetChannel, ChannelJoin

urlpatterns = [
    path('channel', ChannelView.as_view()),
    path('create-channel', CreateChannelView.as_view()),
    path('get-channel', GetChannel.as_view()),
    path('join-channel', ChannelJoin.as_view())
]
