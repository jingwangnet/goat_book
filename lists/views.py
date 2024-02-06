from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List


# Create your views here.
def home_page(request):
    return render(request, "lists/home.html")


def new_list(request):
    new_list = List.objects.create()
    Item.objects.create(text=request.POST["new_item"], list=new_list)
    return redirect("/lists/the-only-url/")


def view_list(request):
    context = {"items": Item.objects.all()}
    return render(request, "lists/list.html", context)
