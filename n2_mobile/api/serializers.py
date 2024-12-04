from rest_framework import serializers
from .models import Geo, Address, Company, User, Post, Comment, Album, Photo, Todo

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'phone', 'website', 'address', 'company']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        company_data = validated_data.pop('company')
        geo_data = address_data.pop('geo')

        geo = Geo.objects.create(**geo_data)

        address = Address.objects.create(geo=geo, **address_data)

        company = Company.objects.create(**company_data)

        user = User.objects.create(address=address, company=company, **validated_data)

        return user

    def update(self, instance, validated_data):

        address_data = validated_data.pop('address', None)
        company_data = validated_data.pop('company', None)


        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if address_data:
            geo_data = address_data.pop('geo', None)
            address = instance.address

            for attr, value in address_data.items():
                setattr(address, attr, value)
            address.save()


            if geo_data:
                geo = address.geo
                for attr, value in geo_data.items():
                    setattr(geo, attr, value)
                geo.save()

        if company_data:
            company = instance.company
            for attr, value in company_data.items():
                setattr(company, attr, value)
            company.save()

        return instance
class CommentSerializer(serializers.ModelSerializer):
    postId = serializers.PrimaryKeyRelatedField(source='post', queryset=Post.objects.all())
    
    class Meta:
        model = Comment
        fields = ['id', 'postId', 'name', 'email', 'body']  

class PostSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    
    class Meta:
        model = Post
        fields = ['id', 'userId', 'title', 'body']  

class AlbumSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    
    class Meta:
        model = Album
        fields = ['id', 'userId', 'title']  

class PhotoSerializer(serializers.ModelSerializer):
    albumId = serializers.PrimaryKeyRelatedField(source='album', queryset=Album.objects.all())
    
    class Meta:
        model = Photo
        fields = ['id', 'albumId', 'title', 'url', 'thumbnail_url'] 

class TodoSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    
    class Meta:
        model = Todo
        fields = ['id', 'userId', 'title', 'completed']  
