from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (GeoViewSet, AddressViewSet, CompanyViewSet, UserViewSet, 
                    PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet, TodoViewSet)

router = DefaultRouter()
router.register(r'geo', GeoViewSet)
router.register(r'address', AddressViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'photo', PhotoViewSet)
router.register(r'todo', TodoViewSet)


