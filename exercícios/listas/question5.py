#Faça um programa que leia 5 nomes de alunos com suas notas. Armazene o nome em uma lista e
# a nota em outra lista na mesma posição. 
#Depois calcule e imprima: 

#1. A média das notas
#2. Os alunos que estão acima da Média
#3. O aluno com maior nota

alunos=[]
notas= []
soma_notas=0
aprovados=[]

for c in range(0,5):
    alunos.append(str(input()))
    notas.append(float(input()))
    soma_notas+= notas[c]

media=soma_notas/5

print("Média: {:.1f}".format(media))

alunos_aprovados=0

for x in range(0,5):
    if notas[x] >media:
        alunos_aprovados+=1
        aprovados.append(alunos[x])
if alunos_aprovados == 1:
    print(f"Acima da média: {aprovados[0]}")
elif alunos_aprovados == 2:
    print(f"Acima da média: {aprovados[0]},{aprovados[1]}")
elif alunos_aprovados == 3:
    print(f"Acima da média: {aprovados[0]},{aprovados[1]},{aprovados[2]}")
elif alunos_aprovados == 4:
    print(f"Acima da média: {aprovados[0]},{aprovados[1]},{aprovados[2]},{aprovados[3]}")
elif alunos_aprovados == 5:
    print(f"Acima da média: {aprovados[0]},{aprovados[1]},{aprovados[2]},{aprovados[3]},{aprovados[4]}")

maior=0
aluno_maior_nota=""

for c in range(0,5):
    if notas[c]>maior:
        aluno_maior_nota= alunos[c]
        maior=notas[c]
print("Maior nota:",aluno_maior_nota)