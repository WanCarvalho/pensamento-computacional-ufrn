#Ana, Bernardo e Caroline são amigos desde que se conheceram na Lagoa do Bonfim, quando ainda eram crianças.
# Nessa época, eles criaram uma competição de jogar pedra na lagoa bem diferente das outras. Enquanto outros
# jogam as pedras tentando fazê-las saltar o maior número de vezes ("quicar" na água), na competição deles
# (entre os três), ganhava quem fizesse a pedra saltar uma certa quantidade que não fosse nem a maior nem
# a menor. Por exemplo, se Ana fizesse a pedra quicar 3 vezes, Bernardo apenas 1 vez e Caroline 2 vezes,
# então Caroline é a vencedora. Se houvesse mais de um valor intermediário, então não haveria vencedor.
#Os três amigos, agora na idade adulta, resolveram criar um jogo online multiplayer no qual uma das mecânicas
# é acertar um valor intermediário entre os valores definidos por outros dois jogadores (obviamente,
# sem conhecê-los). Eles pediram para você implementar essa parte do jogo.
#Entrada
#Seu programa deve ler 3 números inteiros A, B e C, representando os valores definidos por 3 jogadores.
#Saída
#Seu programa deve enviar para a saída (imprimir) "A" se o valor lido em A for um valor intermediário
# entre os valores em B e C, "B" se o valor B for um intermediário entre os demais, "C" se o intermediário
# for o valor C ou "N" se não houver vencedor.

A = int(input())
B = int(input())
C = int(input())

if C > A and A > B or C < A and A < B:
    print('A')
if C > B and B > A or C < B and B < A:
    print('B')
if A > C and C > B or A < C and C < B:
    print('C')
if A == C or B == C or A == B:
    print('N')