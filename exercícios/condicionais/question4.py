#Você entrou em um projeto de iniciação científica voltado a elaborar algoritmos seguros para carros autônomos.
# Por enquanto, a equipe realiza apenas testes/simulações em um ambiente virtual e estão interessados em
# definir um algoritmo que faça o carro dirigir em segurança entre dois outros carros. Sua tarefa inicial é
# desenvolver um programa que indique se um carro deve acelerar ou frear em função da distância que se
# encontra de dois outros carros.
#O ambiente virtual em questão simula uma estrada reta, sem curvas, onde a posição de um carro é definida por
# um único valor, que indica a distância do carro ao início da estrada. Nessa simulação, não é possível ter
# dois carros na mesma posição (dois corpos não ocupam o mesmo local ao mesmo tempo!).
#Seu programa deve indicar para o carro que ele controla para acelerar se houver um carro atrás e outro na
# frente e se o detrás estiver mais próximo do que o da frente. Se for o carro da frente que estiver mais
# próximo, então deve-se mandar frear. Porém, se os carros estiverem equidistantes do carro controlado por
# seu programa ou se ambos estiverem à frente ou atrás, seu programa deve indicar para continuar na mesma
# velocidade (nem acelerar nem frear).
#Entrada
#Seu programa deve ler 3 números inteiros C, C1 e C2 indicando a posição do carro controlado pelo seu
# programa (C) e as posições dos outros dois carros (C1 e C2).
#Saída
#Seu programa deve enviar para a saída (imprimir) "A" se for necessário acelerar, "F" se for necessário frear
# ou "C" se precisar continuar como está (nem acelerar nem frear).

C = int(input())
C1 = int(input())
C2 = int(input())
lista_ordenada = [C, C1, C2]

if C==max(lista_ordenada) or C==min(lista_ordenada):
    print('C')
else:
    lista_ordenada.sort() #coloco as variaveis em ordem crescente (equivalente as posições dos carros), para realizar as operações

    if abs(lista_ordenada[0]-lista_ordenada[1]) > abs(lista_ordenada[1]-lista_ordenada[2]):
        print('F')

    elif abs(lista_ordenada[0]-lista_ordenada[1]) < abs(lista_ordenada[1]-lista_ordenada[2]):
        print('A')

    else:
        print('C')

