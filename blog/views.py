from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.serializers import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer
