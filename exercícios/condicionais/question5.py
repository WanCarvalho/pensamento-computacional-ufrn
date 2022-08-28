# Vamos fazer um  jogo. Agora é o clássico papel, pedra ou tesoura. Nesse jogo cada jogador
# escolhe entre uma das 3 opções: “papel”, “pedra”, ou “tesoura”.  Depois de feitas as escolhas,
# cada jogador revela a sua e a vitória é decidida de acordo com as seguintes regras:

# •	O Papel vence a pedra

# •	A pedra vence a tesoura

# •	A tesoura vence o papel

# •	Se os dois forem iguais é empate

# No programa deste jogo você deve receber como entrada a escolha do jogador 1 e a escolha do jogador 2.
# Eles irão digitar “papel”, “pedra”, ou “tesoura” com letra minúscula mesmo. Você vai decidir quem venceu
# (ou se deu empate) de acordo com as regras que foram expostas.

jogador1=str(input()).strip().lower()
jogador2=str(input()).strip().lower()

if jogador1 == "pedra" and jogador2 == "papel":
    print('Jogador 2 venceu')
elif jogador1 == "papel" and jogador2 == "pedra" :
    print('Jogador 1 venceu')
elif jogador1 == "tesoura" and jogador2 == "papel" :
    print('Jogador 1 venceu')
elif jogador1 == "papel" and jogador2 == "tesoura" :
    print('Jogador 2 venceu')
elif jogador1 == "pedra" and jogador2 == "tesoura" :
    print('Jogador 1 venceu')
elif jogador1 == "tesoura" and jogador2 == "pedra" :
    print('Jogador 2 venceu')
elif jogador1==jogador2:
    print("empate")
