# implementacion del Kahn’s algorithm
# Complejidad: O(N+A) 
# N => # de nodos , A=> # de aristas

def ordenamiento_topologico(grafo):
    lista = []
    aristasEntrantes = {nodo: 0 for nodo in grafo}

    for nodo in grafo:
        for vecino in grafo[nodo]:
            aristasEntrantes[vecino] += 1

    nodosSinAristasEntrantes = [nodo for nodo in aristasEntrantes if aristasEntrantes[nodo] == 0]

    while nodosSinAristasEntrantes:
        primernodo = nodosSinAristasEntrantes.pop(0)
        lista.append(primernodo)
        for vecino in grafo[primernodo]:
            aristasEntrantes[vecino] -= 1
            if aristasEntrantes[vecino] == 0:
                nodosSinAristasEntrantes.append(vecino)

    if len(lista) == len(grafo):
        return lista
    else:
        return "el grafo tiene ciclos"


print("escriba el numero de conexiones entre los nodos")
nodos = input()

if nodos.isdigit():
    grafo = dict()
    print("Escriba las conexiones de los nodos")
    for _ in range(int(nodos)):
        nodo1, nodo2 = map(str, input().split())
        if nodo1 in grafo:
            grafo[nodo1].append(nodo2)
        else:
            grafo[nodo1] = [nodo2]
        if nodo2 not in grafo:
            grafo[nodo2] = []
    print("ordedamiento topologico >>> ", ordenamiento_topologico(grafo))
else:
    exit()

"""
grafo de ejemplo

grafo = {
    'aceite': ['mezcla'],
    'huevo': ['mezcla'],
    'leche': ['mezcla'],
    'mezcla': ['taza', 'jarabe'],
    'plancha': ['taza'],
    'taza': ['voltear'],
    'voltear': ['comer'],
    'jarabe': ['comer'],
    'comer': []
}
"""