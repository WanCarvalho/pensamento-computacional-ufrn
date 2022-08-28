def sequencia (vetor_a, vetor_b):
    
    if len(vetor_a) > len(vetor_b):
        print("N")
        return

    j = 0

    while(j <= len(vetor_b)):
        
        while vetor_b[j] != vetor_a[0]:
            if j < len(vetor_b) - 1:
               j += 1
            else:
                print("N")
                return               

        if len(vetor_a) > len(vetor_b) - j:
            print("N")
            return

        sequencia = 0
        i = 0
        for i in range(len(vetor_a)):
            if vetor_a[i] != vetor_b[i+j]:
                continue
            else:
                sequencia += 1
        
        if sequencia == len(vetor_a):
            print("S")
            return
        else:
            if j < len(vetor_b) - 1:
               j += 1


vetor_a = []
vetor_b = []


for i in range(int(input())):
    vetor_a.append(int(input()))

for i in range(int(input())):
    vetor_b.append(int(input()))


sequencia(vetor_a, vetor_b)

