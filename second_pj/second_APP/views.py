from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from second_APP.models import Post
from second_APP.serializers import PostModelSerializer


# Create your views here.

class GetPostList(APIView):
    def get(self, request):
        data = Post.objects.all()
        serializer = PostModelSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request):
        id = request.data['id']
        instance = Post.objects.get(pk=id)
        serializer = PostModelSerializer(data=request.data , instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class GetPostListGeneric(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

class CreatePostGeneric(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

def test(request):
    return render(request, 'index.html')


class GetPostById(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class UpdatePostById(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

class DeletePostById(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
