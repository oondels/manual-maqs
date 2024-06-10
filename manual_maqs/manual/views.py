from django.shortcuts import loader
from django.http import HttpResponse
import json
import pymongo

def home(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    myDb = myclient["local"]
    manual_maquinas_db = myDb["manual maq"]
    
    context = {
        "manual_maquinas_db": manual_maquinas_db.find(),
    }
    template = loader.get_template("home.html")
    return HttpResponse(template.render(context, request))
