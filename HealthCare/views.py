from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework import status

def HomePage(request):
    return render(request, 'HomePage.html')

class PostListAPI(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        postSerializer = PostSerializer(data=request.data)
        print(postSerializer)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(data=postSerializer.data, status=status.HTTP_201_CREATED)

class PostAPI(APIView):
    def get(self, request, post_id):
        queryset = Post.objects.filter(pk=post_id)
        print(queryset)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)