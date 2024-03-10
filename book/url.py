
from django.urls import path
from book.views.fn_api import get_books
from book.views.api_view import get_books, Booklist

urlpatterns = [
    # fun based view
    path('getbooks', get_books, name="getbooks"),
    
    #api view
     path('getbooks1', get_books , name="getbooks1"),
     path('getbooks2', Booklist.as_view(),name ="getbooks2")
]

