from django.http import JsonResponse
from rest_framework.response import Response
from book.models import Book
import json
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, APIView
from book.serializers import BookModelSerializer


@api_view(http_method_names=["GET","POST"])
def get_books(req):
    if req.method=="GET":
        books = Book.objects.all()
        ser = BookModelSerializer(books, many=True)
        return Response(ser.data)
    
    if req.method=="POST":
        serializer = BookModelSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse({"success":"False"})
        
class Booklist(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        ser = BookModelSerializer(books, many = True)
        return Response(ser.data)
    
    def post(self, request, format= None):
        data = request.data
        serializer = BookModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

            
            
        
    