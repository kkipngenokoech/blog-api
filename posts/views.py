from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post
from .serializers import PostSerializer
# Create your views here.
class IndexView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
