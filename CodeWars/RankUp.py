# Funções para resolução dos Katas de nível RankUp

# Retorna array sem os numeros contidos na segunda array
def removeNumerosLista(listaOriginal, listaRemover):
    return [x for x in listaOriginal if x not in listaRemover]


# Constroi arvore com *
def constroiArvore(andares):
    return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]


# Retorna ( se string so possui 1 ocorrencia da letra na palavra e ) se possui mais
def retornaParenteses(word):
    return ''.join('(' if word.casefold().count(word[i].casefold()) == 1 else ')' for i in range(0, len(word)))
