#Descrição: um sistema web vende camisetas nos tamanhos: P, M, e G, nas cores azul ,
# ou na cor verde. Estas são as quantidades no estoque: na cor azul P(10), M(7), G(5);
# na cor verde P(12), M(5), G(4). Crie um programa para dar baixa do estoque das camisetas
# vendidas no site. O usuário do programa deverá passar o código da cor (A ou V), e em seguida
# passará a quantidade de camisas vendidas dos tamanhos P, M e G, respectivamente. O programa
# deve imprimir a quantidade de cada camisa, para as duas cores, ainda estão no estoque. Se por
# acaso o usuário digitar uma quantidade de camisas maior que a disponível no estoque, deve aparecer
# o estoque que ainda tem e um alerta "quantidade não disponível"

#Entradas: 
#código de uma das cores (A ou V), seguido de três números inteiros, que são as quantidades de
# camisas vendidas nos tamanhos P, M e G.    

#Saídas:  deve imprimir:

#•	As quantidades de camisetas no estoque, para cada tamanho e cada cor. 

#•	Se o numero de camisetas vendidas for maior que o disponível no estoque, deve aparecer com
# o estoque atual e a seguinte mensagem: “quantidade não disponível"

cod = str(input()).strip().upper()
P = int(input())
M =int(input())
G = int(input())

if cod== "A":
    if P <=10:
        print("P(A):{}".format(10- P))
    else:
        print('P(A):10-"Quantidade não disponível".')
    if M <=7:
        print("M(A):{}".format(7 - M))
    else:
        print('M(A):7- "Quantidade não disponível".')
    if G <= 5:
        print("G(A):{}".format(5 - G))
    else:
        print('G(A):5-"Quantidade não disponível".')
    print("P(V):12")
    print("M(V):5")
    print("G(V):4")
elif cod == "V":
    print("P(A):10")
    print("M(A):7")
    print("G(A):5")
    if P <=12:
        print("P(V):{}".format(12 - P))
    else :
        print('P(V):12-"Quantidade não disponível".')
    if M <=5:
        print("M(V):{}".format(5 - M))
    else:
        print('M(V):5 - "Quantidade não disponível".')
    if G <= 4:
        print("G(V):{}".format(4 - G))
    else:
        print('G(V):4-"Quantidade não disponível".')