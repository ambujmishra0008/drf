from django.http import JsonResponse
from book.models import Book
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_books(req):
    if req.method=="GET":
        books = Book.objects.all()
        booklist = [book.title for book in books]
        res = {"books": booklist}
        return JsonResponse(res)
    if req.method=="POST":
        json_data = json.loads(req.body.decode('utf-8'))
        print(json_data)
        book = Book.objects.create(**json_data)
        return JsonResponse({"success":"True"})
    
    return JsonResponse({"success":"False"})
        