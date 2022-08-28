#Uma das atribuições da Confederação Brasileira de Atletismo é a organização de competições
# nacionais incluindo detalhes como quando, onde e quais atletas irão competir.

#Parte das provas de atletismo são efetuadas numa área especial denominada de pista de atletismo
# que é dividida em 8 raias de modo que cada atleta é alocada uma raia individual e assim ele executará
# toda a prova nessa raia sem atrapalhar os demais. Logo, somente 8 atletas podem competir ao mesmo tempo,
# o que é chamado de série, de modo que uma competição pode ter uma ou mais séries.

#Você deve desenvolver um programa para determinar quantas séries a prova de 100 metros rasos deve ter.
# Porém, somente os atletas mais rápidos devem ser aptos a competir, isto é, somente os atletas que
# correram os 100 metros em um tempo inferior ou igual ao estabelecido para inscrição na competição.
# Desse modo, a primeira entrada do programa será o tempo máximo que o atleta pode ter alcançado para
# estar apto a competir.

#Em seguida, o programa irá receber uma quantidade indeterminada de inscrições até que o valor - 1.0
# seja apresentado. Cada inscrição consiste em um único valor correspondente ao tempo em segundos
# que o atleta correu nos 100 metros registrado até a terceira casa decimal.

#O programa deve apresentar como saída a quantidade total de atletas aptos a competir e logo em
# seguida a quantidade de séries necessárias para realização da prova de 100 metros.

T = float(input())
inscricoes = []
qnt_atletas = 0

limite = -1
i = 0

while(i != limite):
    inscricoes.append(float(input()))

    if(inscricoes[i] < T and inscricoes[i] != -1):
        qnt_atletas += 1
    if(inscricoes[i] == -1):
        i = -2

    i += 1

print(qnt_atletas)

if(qnt_atletas%8 == 0):
    print(int(qnt_atletas/8))
else:
    print(int(qnt_atletas/8)+1)