#Um triângulo só é possível se um lado não é maior que a soma dos outros dois.
#Escreva um programa que recebe três números inteiros como os tamanhos dos três lados
# de um triângulo e verifica se estes tamanhos podem formar um triângulo. Se for possível
# formar um triângulo, o programa deve escrever "possível". Caso contrário, deve escrever "impossível".

lado1=int(input())
lado2=int(input())
lado3=int(input())

x1 = lado1+lado2
x2 = lado2+lado3
x3 = lado1+lado3

if x1<lado3:
    print("impossivel")
elif x2<lado1:
    print("impossível")
elif x3<lado2:
    print("impossível")
else:
    print("possível")