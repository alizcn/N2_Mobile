from rest_framework.response import Response
from rest_framework import viewsets
from .models import Geo, Address, Company, User, Post, Comment, Album, Photo, Todo
from .serializers import (GeoSerializer, AddressSerializer, CompanySerializer, 
                          UserSerializer, PostSerializer, CommentSerializer, 
                          AlbumSerializer, PhotoSerializer, TodoSerializer)
from django.core.cache import cache

class GeoViewSet(viewsets.ModelViewSet):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer
    def retrieve(self, request, *args, **kwargs):
        geo_id = kwargs.get('pk')
        cache_key = f'geo_{geo_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    def retrieve(self, request, *args, **kwargs):
        address_id = kwargs.get('pk')
        cache_key = f'address_{address_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    def retrieve(self, request, *args, **kwargs):
        company_id = kwargs.get('pk')
        cache_key = f'company_{company_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        cache_key = f'user_{user_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def retrieve(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        cache_key = f'post_{post_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def retrieve(self, request, *args, **kwargs):
        comment_id = kwargs.get('pk')
        cache_key = f'comment_{comment_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    def retrieve(self, request, *args, **kwargs):
        album_id = kwargs.get('pk')
        cache_key = f'album_{album_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    def retrieve(self, request, *args, **kwargs):
        photo_id = kwargs.get('pk')
        cache_key = f'photo_{photo_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def retrieve(self, request, *args, **kwargs):
        todo_id = kwargs.get('pk')
        cache_key = f'todo_{todo_id}'

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=900)

        return response
