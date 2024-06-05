import json

with open("manual_maqs_noSQL.json", "r", encoding="utf-8") as manual_maquinas_file:
    manual_maquinas = json.load(manual_maquinas_file)
    
    for i in manual_maquinas["Montagem"]["Máquina de aplicar hot melt rolo 150 mm / 300 mm / 320 mm."]["Defeito 01 – Não liga"]:
        print(i)



