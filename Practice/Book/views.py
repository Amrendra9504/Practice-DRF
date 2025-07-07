from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from Book.models import Author, Publisher, Book
from Book.serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404

class AuthorList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response({
            "status": True,
            "message": "Data has been fetched successfully",
            "data": serializer.data
        })
    
    def post(self, request):
        _data = request.data
        serializer = AuthorSerializer(data = _data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AuthorDetails(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        aut = self.get_object(pk)
        serializer = AuthorSerializer(aut)
        return Response({
            "status": True,
            "message": "Data has been fetched successfully",
            'data': serializer.data
        })
    
    def put(self, request, pk):
        aut = self.get_object(pk)
        _data = request.data
        serializer = AuthorSerializer(aut, data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Data has been updated successfully",
                "data": serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        aut = self.get_object(pk)
        aut.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        bk = Book.objects.all()
        serializer = BookSerializer(bk, many=True)
        return Response({
            "status": True,
            "message": "Data has been fetched successfully",
            "data": serializer.data
        })