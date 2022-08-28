#Um número é dito perfeito se é igual à soma de todos os seus divisores
#próprios (todos os divisores menos ele). Por exemplo, como os divisores
#próprios de 6 são 1, 2, 3 e e 1 + 2 + 3 = 6, 6 é perfeito. Escreva um programa
#que diga se o número é perfeito ou não.

numero = int(input())
divisores = []

for i in range(1, numero-1):
    if(numero%i == 0):
        divisores.append(i)

if(sum(divisores) == numero):
    print("número perfeito")
else:
    print("número não é perfeito")