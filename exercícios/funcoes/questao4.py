def progressao (trecho):
    
   menor = min(trecho)

   progressao = []

   for i in range(len(trecho)):
       progressao.append(trecho[i] - menor)

   return progressao


trecho1 = []
trecho2 = []


for i in range(int(input())):
    trecho1.append(int(input()))

for i in range(int(input())):
    trecho2.append(int(input()))


progressao1 = progressao(trecho1)
progressao2 = progressao(trecho2)

sequencia = 0

for i in range(len(progressao1)):
    if progressao1[i] == progressao2[i]:
        sequencia += 1
    else:
        break

if sequencia == len(progressao1):
    print("S")
else:
    print("N")


