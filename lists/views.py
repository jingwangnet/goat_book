from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


# Create your views here.
def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST["new_item"])
        return redirect("/")
    context = {"new_item_text": request.POST.get("new_item", "")}
    return render(request, "lists/home.html", context)
