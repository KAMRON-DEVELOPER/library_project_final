from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, APIView
from rest_framework.viewsets import ModelViewSet


# VIEWSET AND ROUTER
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# LIST, CREATE   
class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookListApiView(APIView):
    
#     def get(self, request):
#         books = Book.objects.all()
#         serializer_data = BookSerializer(books, many = True).data
#         data = {
#             'status' : f"returned {len(books)} books",
#             'books' : serializer_data
            
#         }
#         return Response(data)

    
class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# class BookCreateApiView(APIView):
    
#     def post(self, request):
#         data = request.data
#         serializer = BookSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {"status" : 'Book are saved...'}
#             return Response(data)


# BOOK DETAIL, UPDATE, DELETE
class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# class BookDetailApiView(APIView):
    
#     def get(self, request, pk):
#         book = Book.objects.get(id=pk)
#         serializer_data = BookSerializer(book).data
#         data = {"status":'successfull', "book":serializer_data}
#         return Response(data)
    

class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# class BookUpdateApiView(APIView):
#     def put(self, request, pk):
#         book = get_object_or_404(Book.objects.all(), id=pk)
#         data = request.data
#         serializer = BookSerializer(instance=book, data=data, partial=True)
#         if serializer.is_valid():
#             book_saved = serializer.save()
#         return Response({"status" : True, "message" : f"{book_saved} updated"})
    

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookDeleteApiView(APIView):
    
#     def delete(self, request, pk):
#         try:
#             book = Book.objects.get(id=pk)
#             book.delete()
#             return Response({'status': True, 'message' : 'successfully deleted'})
#         except Exception:
#             return Response({'status': False, 'message' : 'book is not found'})
            
    
    
# LIST AND CREATE 
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# DELETE AND CREATE 
class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer








# function view yozish tavsiya etilmaydi!
# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
    
#     return Response(serializer.data)

