estado_inicial = '0'
numero_de_estados = input()  # linha 1 numero de estados
simbolos_terminais = input()  # linha 2 entrar com a quantidade de simbolos terminais seguida dos elementos
simbolos_de_fita = input()  # linha 3 entrar com a quantidade de simbolos de pilha seguida dos elementos
estado_de_aceitacao = input()  # linha 4 entrar com o índice do estado de aceitação
numero_de_transicoes = int(input())  # linha 5 numero de transicoes da maquina
tabela_transicoes = {}
for i in range(numero_de_transicoes):  # receber as transicoes
    entrada = input()
    elementos_da_entrada = entrada.split()
    estado_de_partida = elementos_da_entrada[0]
    ler_da_fita = elementos_da_entrada[1]
    estado_destino = elementos_da_entrada[2]
    escrever_na_fita = elementos_da_entrada[3]
    movimento_do_cursor = elementos_da_entrada[4]

    transicao = [(ler_da_fita, estado_destino, escrever_na_fita, movimento_do_cursor)]
    if estado_de_partida not in tabela_transicoes.keys():
        tabela_transicoes[estado_de_partida] = []
    tabela_transicoes[elementos_da_entrada[0]].extend(transicao)

numero_de_cadeias = int(input())  # Depois das t transicoes, na linha seguinte e dado o numero c de cadeias de entrada que serao avaliadas

for i in range(numero_de_cadeias):
    cadeia = input()  # Nas proximas c linhas serao fornecidas as cadeias de entrada (uma por linha)
    fita = list(cadeia)  # Assuma que sempre a cadeia de entrada é colocada na primeira posição da fita, e em seguida, temos um símbolo em branco B
    fita.append('B')
    cadeia_valida = False
    if fita == ['-'] and estado_inicial == estado_de_aceitacao:
        cadeia_valida = True
    elif not fita == ['-']:
        posicao_do_cursor = 0 #posicao inicial do cursor
        estado_atual = estado_inicial
        while True:  # cada ciclo uma transicao
            if estado_atual == estado_de_aceitacao:
                cadeia_valida = True
                break
            transicao_valida = False
            for transicao in tabela_transicoes[estado_atual]:  # para cada transicao mapeada do estado atual
                simbolo_da_fita = transicao[0]
                if simbolo_da_fita == fita[posicao_do_cursor]:  # se existe o movimento para o simbolo apontado pelo cursor
                    transicao_valida = True
                    estado_destino = transicao[1]
                    estado_atual = estado_destino
                    escrever_na_fita = transicao[2]
                    fita[posicao_do_cursor] = escrever_na_fita
                    movimento_do_cursor = transicao[3]
                    if movimento_do_cursor == 'D':  # move para a direita
                        posicao_do_cursor += 1
                    elif movimento_do_cursor == 'E':  # move para a esquerda
                        posicao_do_cursor -= 1
                    break
            if not transicao_valida:  # se a transicao nao esta mapeada
                break
    if cadeia_valida:
        print('aceita')
    else:
        print('rejeita')

