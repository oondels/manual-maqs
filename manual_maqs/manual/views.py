from django.shortcuts import loader
from django.http import HttpResponse
import json

def home(request):
    with open("../maqs_DB/manual_maqs_noSQL.json", "r", encoding="UTF-8") as manual_maquinas:
        manual_maquinas_db = json.load(manual_maquinas)
    
    context = {
        "manual_maquinas_db": manual_maquinas_db,
    }
    template = loader.get_template("home.html")
    return HttpResponse(template.render(context, request))
