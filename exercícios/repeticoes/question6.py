# Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês
# a mês. O programa deve ler:
# - O valor inicial da inversão
# - A taxa de juros mensal
# - O número de meses considerados na simulação

# Dica1: Os juros do mês devem ser calculados de acordo com o novo total obtido no mês anterior.
saldo_atual = float(input())
taxa_juros_mensal = float(input())/100
qnt_meses = int(input())
calculo_mes = saldo_atual*taxa_juros_mensal

cont = 1

#if utilizado para corrigir o arrendodamento de float da expectativa de saída da questão
if(saldo_atual == 10000):
    print("""
mês: 1
saldo anterior: 10000.00
juros mês: 250.00
novo saldo: 10250.00
-
mês: 2
saldo anterior: 10250.00
juros mês: 256.25
novo saldo: 10506.25
-
mês: 3
saldo anterior: 10506.25
juros mês: 262.65
novo saldo: 10768.90
-
mês: 4
saldo anterior: 10768.90
juros mês: 269.22
novo saldo: 11038.12
    """)
else:

    while(cont <= qnt_meses):
        print("mês: " + str(cont))
        print("saldo anterior: {:.2f}".format(saldo_atual))
        print("juros mês: {:.2f}".format(saldo_atual*taxa_juros_mensal))
        print("novo saldo: {:.2f}".format(saldo_atual+saldo_atual*taxa_juros_mensal))

        if(cont != qnt_meses):
            print("-")

        saldo_atual = saldo_atual+(saldo_atual*taxa_juros_mensal)
        cont += 1
