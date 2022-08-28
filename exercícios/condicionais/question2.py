#O Restaurante Universitário (RU) da UFRN reabriu recentemente. Porém, em razão da restrição de ocupação
# definida nos protocolos de Biossegurança da Universidade, o RU não consegue oferecer a mesma quantidade
# de refeições diárias que oferecia antes da pandemia (cerca de 4.500 refeições/dia). Por causa disso,
# a Pró-Reitoria de Assuntos Estudantis (Proae) vai fornecer um auxílio alimentação aos estudantes carentes
# contemplados no edital de acesso ao RU. Porém, o valor que a universidade com esse propósito também é limitado. É possível que o valor do auxílio definido para os alunos contemplados ultrapasse o valor que a universidade recebe para esse propósito.
#Para fazer uma estimativa, a Pró-reitoria solicitou pra você um programa que indique se os recursos
# recebidos são suficientes ou não para um determinado valor de auxílio e uma determinada quantidade de alunos.
#Entrada
#Seu programa deve ler 3 números inteiros R, A e N, representando em R$ respectivamente o total de recursos
# recebidos pela universidade (R), o valor do auxílio alimentação (A) e o número de alunos contemplados com
# o auxílio (N).
#Saída
#Seu programa deve enviar para a saída (imprimir) "S" se for possível fornecer o auxílio a todos os alunos
# contemplados ou "N" se não for possível.

R = int(input())
A = int(input())
N = int(input())

if A != 0:
    if R // A < N:
        print ('N')
    if R // A > N:
  	    print('S')
if R // A == N:
  	print('S')
else:
  print('S')
