from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import BookSerializer

class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer