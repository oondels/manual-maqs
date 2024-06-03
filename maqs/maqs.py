import pandas as pd

with open('maqs.txt', encoding='utf 8') as manual:
    manual_tpm = manual.read()  

    maqs_defeito = [list.split('\n') for list in manual_tpm.split('\n\n') if list]

    maqs_problem_solution = {}
    solucao_defeito_maquinas = []
    
    lista_montagem = []
    lista_costura = []
    lista_apoio = []
    lista_serigrafia = []
    lista_pre = []
    
    for list_maquina in maqs_defeito:
        maqs_problem_solution[list_maquina[0]] = {}
    
    count=0
    for posicao, list_maquina in enumerate(maqs_defeito):
        count += 1
        maqs_problem_solution[list_maquina[0]][list_maquina[1]] = list_maquina[2:]
        if 'Itens a Verificar' in list_maquina:
            maqs_problem_solution[list_maquina[0]][list_maquina[count]] = list_maquina[count+1:]

db = pd.read_csv("./maquinas_setor/maquinas.csv")
print(db.head())