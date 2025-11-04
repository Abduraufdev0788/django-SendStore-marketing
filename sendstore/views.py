from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home_page(request: HttpRequest):
    return render(request=request, template_name="index.html")


