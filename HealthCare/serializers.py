from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Post
        fields = ('content1', 'content2', 'content3', 'create_date')