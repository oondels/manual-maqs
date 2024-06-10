import json
import pymongo

with open("manual_maqs_noSQL.json", "r", encoding="utf-8") as manual_maquinas_file:
    manual_maquinas = json.load(manual_maquinas_file)
    count = 0
    for i in manual_maquinas:
        for j in manual_maquinas[i]:
            count += 1

myclient = pymongo.MongoClient("mongodb://localhost:27017")
myDb = myclient["local"]
manual_maq = myDb["manual maq"]
print(type(manual_maq))
for i in manual_maq.find():
    print(i)
