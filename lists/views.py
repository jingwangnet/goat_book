from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


# Create your views here.
def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST["new_item"])
        return redirect("/lists/the-only-url/")
    context = {"items": Item.objects.all()}
    return render(request, "lists/home.html", context)


def view_list(request):
    context = {"items": Item.objects.all()}
    return render(request, "lists/list.html", context)
