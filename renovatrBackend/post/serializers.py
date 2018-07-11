from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from post.models import Post


class ListSerializer(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'image']

    def get_author(self, object):
        return str(obj.author.username)


class DetailSerializer(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'image']
        lookup_field = 'pk'

    def get_author(self, object):
        return str(obj.author.username)

class PostCreateSerializer(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
         model = Post
         fields = ['title', 'content', 'author', 'published']

    def get_author(self, obj):
        return str(obj.author.username)

    # Think this can be refactored...
