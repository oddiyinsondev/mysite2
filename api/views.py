from .serializers import PostSerializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Post
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response

class PostList(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Post.published.all()
    serializer_class = PostSerializers

class Postdetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAdminUser, )
    queryset = Post.published.all()
    serializer_class = PostSerializers


class Apiviews(APIView):
    permission_classes = (IsAdminUser, )
    def get(self, request):
        users = User.objects.all().values()
        return Response({'users':users}) 
     