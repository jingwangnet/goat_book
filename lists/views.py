from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List


# Create your views here.
def home_page(request):
    return render(request, "lists/home.html")


def new_list(request):
    new_list = List.objects.create()
    Item.objects.create(text=request.POST["new_item"], list=new_list)
    return redirect(f"/lists/{new_list.pk}/")


def view_list(request, pk):
    new_list = List.objects.get(pk=pk)
    context = {"list": new_list}
    return render(request, "lists/list.html", context)


def add_item(request, pk):
    list_ = List.objects.get(pk=pk)
    Item.objects.create(text=request.POST["new_item"], list=list_)
    return redirect(f"/lists/{list_.pk}/")
