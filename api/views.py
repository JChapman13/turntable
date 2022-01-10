from django.shortcuts import render
from rest_framework import generics, status
from .serializers import ChannelSerializer, CreateChannelSerializer
from .models import Channel
from rest_framework.views import APIView
from rest_framework.response import Response


class ChannelView(generics.CreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class GetChannel(APIView):
    serializer_class = ChannelSerializer
    lookup_url_kwarg = 'code'

    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            channel = Channel.objects.filter(code=code)
            if len(channel) > 0:
                data = ChannelSerializer(channel[0]).data
                data['is_host'] = self.request.session.session_key == channel[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Channel Not Found': 'Invalid Channel Code.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Code paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)

class ChannelJoin(APIView):
    lookup_url_kwarg = 'code'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        code = request.data.get(self.lookup_url_kwarg)
        if code != None :
            channel_result = Channel.objects.filter(code=code)
            if len(channel_result) > 0:
                channel = channel_result[0]
                self.request.session['channel_code'] = code
                return Response({'message': 'Channel Joined!'}, status=status.HTTP_200_OK)
            return Response({'Bad Request': 'Invalid channel code'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Bad Request': 'Invalid post data, did not find a code key'}, status=status.HTTP_400_BAD_REQUEST)


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
                self.request.session['channel_code'] = channel.code
                return Response(ChannelSerializer(channel).data, status=status.HTTP_200_OK)
            else: 
                channel = Channel(host=host, guest_pause = guest_pause, votes_skip= votes_skip)
                channel.save()
                self.request.session['channel_code'] = channel.code
                return Response(ChannelSerializer(channel).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
