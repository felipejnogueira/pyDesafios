# Funções de nível iniciante no CodeChef

# $10 por km e no mínimo $3000 no dia
# https://www.codechef.com/viewsolution/72445518
def carroAlugado():
    # Recebe quantidade de testes a serem feitos
    testes = int(input())

    # Loop para receber valores
    for i in range(testes):
        # Recebe variavel de km's
        kms = int(input())
        print(kms * 10 if kms * 10 > 3000 else 3000)


# Retorna string (YES / NO) se tem dinheiro para pagar a conta
def pagandoDate():
    # Quantidade de testes
    testes = int(input())

    # Loop para resolver testes
    for i in range(testes):
        # Recebe valores | '1 1' / '2 3'
        val = input().split(' ', 2)
        print('YES' if int(val[0]) >= int(val[1]) else 'NO')
