# Retorna o dobro de cada número dentro da array
def dobroArray(array):
    for i in range(0, len(array)):
        array[i] = array[i] * 2

    return array


# Retorna quantidade de folhas necessárias para copiar a lição para todos
def paperwork(alunos, paginas):
    return alunos * paginas if alunos > 0 and paginas > 0 else 0


# Retorna se carro consegue chegar até o posto mais próximo
def zeroGasolina(distancia, metrosGalao, restoGasolina):
    return restoGasolina * metrosGalao >= distancia


# Retorna array com números invertidos pisitiva e negativamente
def numerosInvertidos(array):
    return [-x for x in array]


# Retorna número oposto positivo/negativo
def numeroInvertido(num):
    return num * 1


# Retorna soma de números na array excluindo menor e maior números
# Retorna 0 se array estiver vazio ou com apenas 1 número
def somaArraySemExtremos(array):
    return 0 if array is None or len(array) <= 1 else sum(array) - max(array) - min(array)