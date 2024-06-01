from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    maqs = {
        "name": "Forno Reativador",
        "Causas": "Botão emergência ativado"
    }
    context = { 
        'maqs': maqs
    }
    template = loader.get_template("home.html")
    return HttpResponse(template.render(context, request))
