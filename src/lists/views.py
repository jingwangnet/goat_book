from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Item, List


# Create your views here.
def home_page(request):
    return render(request, "lists/home.html")


def new_list(request):
    new_list = List.objects.create()
    item = Item(text=request.POST["new_item"], list=new_list)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        new_list.delete()
        context = {"error": "You can't have an empty list item"}
        return render(request, "lists/home.html", context)
    return redirect(new_list)


def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    error = None
    context = {"list": list_}
    if request.method == "POST":
        try:
            item = Item(text=request.POST["new_item"], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            context.update({"error": "You can't have an empty list item"})
    return render(request, "lists/list.html", context)
