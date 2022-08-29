# Funções para resolução dos Katas de nível RankUp

def removeNumerosLista(lista = [], remover = []):
    for itemLista in lista:
        for itemRemove in remover:
            if itemLista == itemRemove:
                lista.pop(itemLista)
    return lista
