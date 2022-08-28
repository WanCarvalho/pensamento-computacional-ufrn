#Você ganhou uma bolsa em um projeto no Instituto Internacional de Física da UFRN para trabalhar com
#Astrofísica. No projeto, uma grande quantidade de dados é coletada e os dados devem ser processados
#por filtros, descartando os "dados falsos", oriundos normalmente de erros de leitura.
#Sua primeira tarefa solicitada foi escrever um filtro simples, que tem como entrada valores inteiros
#quaisquer e como saída os valores(lidos da entrada) que se encontram em um dado intervalo. Os seja, seu
#filtro deixaria "passar" apenas os valores no intervalo especificado.

#Entrada
#Seu programa deve ler inicialmente 2 números inteiros, MIN e MAX, que representam respectivamente os
#valores mínimo e máximo do intervalo do filtro(incluindo eles). Depois ler um terceiro número inteiro, N,
#que indica a quantidade de dados que serão enviados para o filtro. Em seguida, seu programa deve ler N
#valores inteiros correspondente aos dados que passarão pelo filtro.

#Saída
#Seu programa deve enviar para a saída padrão(imprimir) apenas os valores enviados na entrada que se
#encontram no intervalo fechado[MIN: MAX], na ordem em que eles foram lidos na entrada.

min = int(input())
max = int(input())
N = int(input())
lista_num = []
intervalo_num = []

for c in range(0, N):
    lista_num.append (int(input()))
    if min <= lista_num[c] and lista_num[c] <= max:
        intervalo_num.append (lista_num[c])

contador = 0
while contador < len(intervalo_num):
    print(intervalo_num[contador])
    contador += 1