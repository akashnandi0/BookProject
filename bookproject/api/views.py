from django.shortcuts import render
from .serializers import BookSerializer, AuthorSerializer
from api.models import Book, Author
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

class BookListView(ListAPIView):
    search_fields = ['author_name__author_name','title']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class BookRetrieveView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BookDestroyView(DestroyAPIView):
    queryset = Book.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser] 