#Faça um programa  para ler o ano de nascimento de uma pessoa, calcular e mostrar
#sua idade e, também, verificar e mostrar se ela já tem idade para votar (16 anos ou mais) 
#e para conseguir a Carteira de Habilitação (18 anos ou mais).
#ps: considere apenas o ano de nascimento 

ano_nascimento = int(input())
idade= 2022-ano_nascimento

print(idade ,"anos")
if idade >= 18:
    print("Pode votar e dirigir")
elif idade >= 16 and idade <= 18:
    print("Pode votar e não pode dirigir")
else:
    print("Não pode votar e não pode dirigir")