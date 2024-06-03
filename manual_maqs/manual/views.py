from django.shortcuts import loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())
