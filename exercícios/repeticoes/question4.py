# Agora que você entrou no BTI, começaram a aparecer oportunidades de trabalho em várias frentes.
# Uma delas é na área de jogos, sua grande paixão. Porém, seu primeiro trabalho não foi beeeemmm como você pensou.
# Enquanto você achava que ia começar trabalhando com gráficos, personagens e tudo mais... te colocaram para
# fazer análise de dados das partidas(você não sabia o quanto isso era importante...)
# Sua primeira tarefa foi organizar o tempo gasto por um jogador em períodos de tamanho fixo. Assim, seu programa poderá,
# por exemplo, ler dados de um ano inteiro e fazer relatórios mensais(período de 30 dias), semanais(7 dias) ou outro período
# qualquer. Os dados lidos são diários e representam o tempo de uso do jogo, podendo ser 0 se o jogador não usar o jogo no dia
# correspondente. Seu programa deverá fornecer, para cada período, o total do tempo jogado e quantos dias o jogador usou o jogo.

# Entrada
# Seu programa deverá ler inicialmente um número inteiro P que indica a quantidade de períodos do relatório.
# Em seguida, deverá ler outro número inteiro D, que indica a quantidade de dias de cada período. Por fim, seu
# programa deverá ler P x D valores inteiros, que representam o tempo de jogos em cada um dos dias.

# Saída
# Seu programa deve enviar para a saída padrão(imprimir), para cada período, duas linhas.
# A primeira deverá estar no formato "TEMPO DE JOGO: t", onde t é a soma dos tempos de jogo no período.
# A segunda deverá estar no formato "DIAS DE JOGO: d", onde d é a quantidade de dias em que o jogador fez uso do jogo.
# Após cada período, seu programa deverá imprimir uma nova linha com "-".
# Obs: Há um(e apenas um) espaço em branco entre o caractere ":" e o valor inteiro seguinte.

P = int(input())  # QNT DE PERIODOS
D = int(input())  # QNT DE DIAS DE CADA P

contador = 0
while (contador < P):
    time_game = 0
    days_game = 0
    for c in range(0, D):
        min_game = int(input())
        time_game += min_game
        if min_game != 0:
            days_game += 1
    print("TEMPO DE JOGO:", time_game)
    print("DIAS DE JOGO:", days_game)
    print("-")
    contador += 1
