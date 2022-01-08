from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, serializers, status
from .serializers import ChannelSerializer, CreateChannelSerializer
from .models import Channel
from rest_framework.views import APIView
from rest_framework.response import Response


class ChannelView(generics.CreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class CreateChannelView(APIView):
    serializer_class = CreateChannelSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_pause = serializer.data.get('guest_pause')
            votes_skip = serializer.data.get('votes_skip')
            host = self.request.session.session_key
            queryset = Channel.objects.filter(host=host)
            if queryset.exists():
                channel = queryset[0]
                channel.guest_pause = guest_pause
                channel.votes_skip = votes_skip
                channel.save(update_fields=['guest_pause', 'votes_skip'])
                return Response(ChannelSerializer(channel).data, status=status.HTTP_200_OK)
            else: 
                channel = Channel(host=host, guest_pause = guest_pause, votes_skip= votes_skip)
                channel.save()
                return Response(ChannelSerializer(channel).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
