from django.shortcuts import render,HttpResponse,redirect
from app.models import BooksForm,Books
# Create your views here.

def index(request):  
    book=BooksForm()
    if request.method=="POST":
        book=BooksForm(request.POST) 
        if book.is_valid():
            book.save()
            return redirect("/")
    
    return render(request,'index.html',{"title":'My Home Page',"book":book})
