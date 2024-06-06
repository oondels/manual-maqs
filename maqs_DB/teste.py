import json

with open("manual_maqs_noSQL.json", "r", encoding="utf-8") as manual_maquinas_file:
    manual_maquinas = json.load(manual_maquinas_file)
    count = 0
    for i in manual_maquinas:
        for j in manual_maquinas[i]:
            count += 1
            
    print(count)


