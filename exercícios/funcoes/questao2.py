def intercessao (tela, caixa):
    
    x0 = tela[0]
    y0 = tela[1]
    x1 = tela[2]
    y1 = tela[3]
    
    x_0 = caixa[0]
    y_0 = caixa[1]
    x_1 = caixa[2]
    y_1 = caixa[3]

    if (x_0 < x0 and x_1 < x0) or (x_0 > x1 and x_1 > x0):
        return
    if (y_0 > y0 and y_1 > y0) or (y_0 < y1 and y_1 < y1): 
        return
    
    if (x_0 < x0 and x_1 > x1) or (x_0 > x0 and x_0 < x1) or (x_1 > x0 and x_1 < x1):
        if (y_0 > y0 and y_1 < y1) or (y_0 < y0 and y_0 > y1) or (y_1 < y0 and y_1 > y1):
            print(str(x_0) + " " + str(y_0) +  " " + str(x_1) + " " + str(y_1)) 



tela = []
total_caixas = 0

for i in range(4):
    tela.append(int(input()))

total_caixas = int(input())

for i in range (total_caixas):
    caixa = []
    for i in range(4):
        caixa.append(int(input()))
    
    intercessao(tela, caixa)




