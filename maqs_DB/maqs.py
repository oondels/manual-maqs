import pandas as pd
import json

with open('maqs.txt', encoding='utf 8') as manual:
    db = pd.read_csv("./maquinas_setor/maquinas.csv")
    manual_tpm = manual.read()  

    maqs_defeito = [list.split('\n') for list in manual_tpm.split('\n\n') if list]

    maqs_problem_solution = {
        "Montagem": {},
        "Apoio": {},
        "Costura": {},
        "Serigrafia": {},
        "Pré Solado": {},
        "Corte Automático": {}
    }
    
    # Função para separar defeitos e Itens a Verificar
    def solucao_defeito(setor):
        count = 0
        for list_maquina in maqs_defeito:
            # `Try` para verificar se a máquina da verificação está no setor, se não tiver ignora a máquina
            try:
                count += 1
                maqs_problem_solution[setor][list_maquina[0]][list_maquina[1]] = list_maquina[2:]
                if 'Itens a Verificar' in list_maquina:
                    maqs_problem_solution[setor][list_maquina[0]][list_maquina[count]] = list_maquina[count+1:]
            except:
                pass
    
    solucao_defeito_maquinas = []
    
    for list_maquina in maqs_defeito:
        # Separando as máquinas por setor
        setor_maq = db[db['Máquinas']==list_maquina[0]]["Setor"].to_string()
        if "Montagem" in setor_maq:
            maqs_problem_solution["Montagem"][list_maquina[0]] = {}
            solucao_defeito("Montagem")
        elif "Costura" in setor_maq:
            maqs_problem_solution["Costura"][list_maquina[0]] = {}
            solucao_defeito("Costura")
        elif "Apoio" in setor_maq:
            maqs_problem_solution["Apoio"][list_maquina[0]] = {}
            solucao_defeito("Apoio")
        elif "Serigrafia" in setor_maq:
            maqs_problem_solution["Serigrafia"][list_maquina[0]] = {}
            solucao_defeito("Serigrafia")
        elif "Pré Solado" in setor_maq:
            maqs_problem_solution["Pré Solado"][list_maquina[0]] = {}
            solucao_defeito("Pré Solado")
        elif "Corte Automático" in setor_maq:
            maqs_problem_solution["Corte Automático"][list_maquina[0]] = {}
            solucao_defeito("Corte Automático")

# Convertendo para formato Json
json_file = json.dumps(maqs_problem_solution, ensure_ascii=False)
with open("manual_maqs_noSQL.json", "w", encoding="utf-8") as manual_noSQL:
    file = manual_noSQL.writelines(json_file)