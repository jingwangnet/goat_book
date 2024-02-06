from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    context = {"new_item_text": request.POST.get("new_item", "")}
    return render(request, "lists/home.html", context)
