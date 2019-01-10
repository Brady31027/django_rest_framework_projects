from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from . import serializer, models, permissions

# Create your views here.
class HelloApiView(APIView):
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Use HTTP methods as function(get, post, patch, put, delete)',
            'Similar to traditional Django View',
            'Gives most control of your app logic',
            'It\'s mapped manually to URLs',
        ]
        return Response({'message': 'Hello!',
                         'an_apiview': an_apiview})

    def post(self, request):
        serializerObj = serializer.HelloSerializer(data=request.data)
        if serializerObj.is_valid():
            name = serializerObj.data.get('name')
            msg = 'Hello {0}'.format(name)
            return Response({'message':msg})
        else:
            return Response(serializerObj.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})

    def delete(self, request):
        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializer.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionalities with less code',
        ]
        return Response({'Message': 'Hello ViewSet!',
                         'a_viewset': a_viewset})

    def create(self, request):
        serializerObj = serializer.HelloSerializer(data=request.data)
        if serializerObj.is_valid():
            name = serializerObj.data.get('name')
            msg = 'Hello {0}'.format(name)
            return Response({'message':msg})
        else:
            return Response(serializerObj.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':' PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnerProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')

class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ this viewset will call built-in apiview to get the auth token """
        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializer.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user_profile = self.request.user) # USERNAME_FIELD ??