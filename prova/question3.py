N = int(input())
notas = []

acima = 0

for i in range(0, N):
    notas.append(float(input()))

media = sum(notas)/N
newList = notas[::-1]

print("Foram lidos",N,"valores")
print(notas)
print("Lista reversa: ",newList)
print("Média dos valores: ",round(media, 2))

for valor_media in notas:  
    if valor_media > media:  
        acima += 1 

print(acima,"valores acima da média",round(media,2))