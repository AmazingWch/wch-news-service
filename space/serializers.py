from rest_framework import serializers
from space.models import Authors, Stories
from django.contrib.auth.models import User, Group


# Serializers define the API representation.
class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['id', 'name', 'username', 'password']


class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ['key', 'headline', 'category', 'region', 'author', 'date', 'details']


# ViewSets define the view behavior.
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
