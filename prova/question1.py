#Entrada

#A única linha da entrada contém um único inteiro N, indicando o consumo de água da residência, em m3

#Saída

#Seu programa deve imprimir uma única linha, contendo o valor da conta de água daquela residência.

N = int(input())
total_conta = 0

if(N <= 10):
    total_conta = 7
elif(N >= 11 and N <=30):
    total_conta = (N-10) * 1 + 7
elif(N >= 31 and N <= 100):
    total_conta = (N-30) * 2 + 27
else:
    total_conta = (N-100) * 5 + 167

print(total_conta)