from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import ChannelSerializer
from .models import Channel

class ChannelView(generics.CreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    

