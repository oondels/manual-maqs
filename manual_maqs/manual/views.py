from django.shortcuts import loader, render
from django.http import HttpResponse
import json

def home(request):
    with open("../maqs_DB/manual_maqs_noSQL.json", "r", encoding="utf-8") as manual_maquinas_db:
        manual_maquinas = json.load(manual_maquinas_db)    
    
    context = {
        "manual_maquinas": manual_maquinas,
    }
    template = loader.get_template("home.html")
    return render(request, 'home.html', {'manual_maquinas': manual_maquinas})
