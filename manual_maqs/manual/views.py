from django.shortcuts import loader, render
from django.http import HttpResponse
import json
from difflib import get_close_matches


def manual_maquinas_view(request):
    with open("../maqs_DB/manual_maqs_noSQL.json", "r", encoding="utf-8") as manual_maquinas_db:
        manual_maquinas = json.load(manual_maquinas_db)    
    
    query = request.GET.get('query', '')
    manual_filtrado = {}

    if query:
        for setor, machines in manual_maquinas.items():
            filtered_details = {}
            # Pesquisa do Setor
            if query.lower() in setor.lower():
                manual_filtrado[setor] = machines
            else:
                # Pesquisa de Máquinas
                for machine, items in machines.items():
                    if query.lower() in machine.lower():
                        filtered_details[machine] = items
                    else:
                        # Pesquisa de Defeitos e Itens a verificar
                        categoria_items = {}
                        for categoria, problemas in items.items():
                            if query.lower() in categoria.lower():
                                categoria_items[categoria] = problemas
                            else:
                                problemas_items = [problema for problema in problemas if query.lower() in problema.lower()]
                                if problemas_items:
                                    categoria_items[categoria] = problemas_items
                        if categoria_items:
                            filtered_details[machine] = categoria_items
                if filtered_details:
                    manual_filtrado[setor] = filtered_details
                    
        # Início da lógica de busca aproximada
        if not manual_filtrado:
            all_texts = [setor for setor in manual_maquinas.keys()]
            for setor, machines in manual_maquinas.items():
                all_texts.extend([machine for machine in machines.keys()])
                for items in machines.values():
                    for categoria, problemas in items.items():
                        all_texts.append(categoria)
                        all_texts.extend(problemas)

            closest_matches = get_close_matches(query, all_texts, n=5, cutoff=0.5)

            for match in closest_matches:
                for setor, machines in manual_maquinas.items():
                    if match.lower() == setor.lower():
                        manual_filtrado[setor] = machines
                    else:
                        filtered_details = {}
                        for machine, items in machines.items():
                            if match.lower() == machine.lower():
                                filtered_details[machine] = items
                            else:
                                categoria_items = {}
                                for categoria, problemas in items.items():
                                    if match.lower() == categoria.lower():
                                        categoria_items[categoria] = problemas
                                    else:
                                        problemas_items = [problema for problema in problemas if match.lower() in problema.lower()]
                                        if problemas_items:
                                            categoria_items[categoria] = problemas_items
                                if categoria_items:
                                    filtered_details[machine] = categoria_items
                        if filtered_details:
                            manual_filtrado[setor] = filtered_details
        # Fim da lógica de busca aproximada
                             
    
    context = {
        'manual_maquinas': manual_maquinas,
        'filtered_manual': manual_filtrado,
        'query': query
    }

    return render(request, 'manual_maquinas.html', context)