# Descrição: A sequencia de Fibonacci é conhecida mundialmente por descrever inúmeros fenômenos
# biológicos. Ela pode ser construída pela fórmula F(n) = F(n-1) + F(n-2) para o n-ésimo termo (n >=2),
# com F(0) = 0 e F(1) = 1. Qualquer termo da sequencia pode ser construído com os termos anteriores.
# Este é um trecho inicial da sequencia (que é infinita): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
# 233, 377, 610, 987, 1597, 2584, ...

# Crie um programa onde que receba dois números inteiros M e D, e que imprima os M primeiros termos da
# sequencia que sejam divisíveis por D.

# Entradas: inteiros M e D.
# Saídas: M primeiros termos da sequencia que sejam divisíveis por D.

M = int(input())
D =int(input())

contador = 0
antecessor = 1
sucessor = 0
total = 0

while True:
    total = sucessor + antecessor
    antecessor = sucessor
    sucessor = total
    if (total%D) == 0:
        print(total)
        contador +=1
        if contador == M:
            break
