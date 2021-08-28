numero_de_estados = input() #linha 1 numero de estados
simbolos_terminais = input() #linha 2 entrar com a quantidade de simbolos terminais seguida dos elementos
simbolos_de_pilha = input() #linha 3 entrar com a quantidade de simbolos de pilha seguida dos elementos
estados_de_aceitacao = []
estados_de_aceitacao.extend(input().split()) #linha 4 entrar com a quantidade de estados de aceitacao seguida dos elementos
estados_de_aceitacao = estados_de_aceitacao[slice(1, int(estados_de_aceitacao[0]) + 1)]

numero_de_transicoes = int(input()) #linha 5 numero de transicoes do automato
tabela_transicoes = {}
for i in range(numero_de_transicoes):
    entrada = input().split()
    transicao = [(entrada[1], entrada[2], entrada[3], entrada[4])]
    if not entrada[0] in tabela_transicoes.keys():
        tabela_transicoes[entrada[0]] = []
    tabela_transicoes[entrada[0]].extend(transicao)
numero_de_cadeias = int(input()) #Depois das t transicoes, na linha seguinte e dado o numero c de cadeias de entrada que serao avaliadas

def computar_cadeias(estado, cadeia, pilha):
    global tabela_transicoes
    global aceito
    if len(cadeia) == 0 or cadeia == '-': #apos processar a cadeia ou se a entrada for a cadeia vazia
        for estado_i in estados_de_aceitacao:
            if estado_i == estado: #se estiver em um dos estados de aceitacao
                aceito = True #sinaliza caso alguma ramificacao terminou aceita
                return 0
    sequencia = [] #armazenar as possiveis ramificacoes
    if estado in tabela_transicoes.keys(): #evitar keyerror
        for transicao_atual in tabela_transicoes[estado]: #para cada transicao possivel mapeada do estado atual
            novo_temporario = [transicao_atual[2]] #lista com estado atual, cadeia a ser processada e pilha

            if transicao_atual[0] != '-':
                if len(cadeia) > 0 and cadeia[0] == transicao_atual[0]:
                    novo_temporario.append(cadeia[1:])
                else:
                    continue
            else:
                novo_temporario.append(cadeia) #nao consome simbolo terminal
            if len(transicao_atual[1]) > 0:
                if len(pilha) > 0 and pilha[0] == transicao_atual[1]:
                    if transicao_atual[3] == '-': #caso de nao adicionar nada a pilha
                        novo_temporario.append(pilha[1:])
                    else:
                        novo_temporario.append(transicao_atual[3] + pilha[1:])
                else:
                    continue

            sequencia.append(novo_temporario) #caso o simbolo terminal e o simbolo da pilha estejam mapeados na transicao salvamos como uma sequencia valida
    if len(sequencia) == 0:
        return 0

    for j in sequencia: #percorre todas as ramificacoes encontradas
        computar_cadeias(j[0], j[1], j[2])
    return 0


for i in range(numero_de_cadeias):
    cadeia = input() #Nas proximas c linhas serao fornecidas as cadeias de entrada (uma por linha)
    aceito = False
    computar_cadeias('0', cadeia, 'Z') #estado inicial e simbolo inicial da pilha
    if aceito:
        print("aceita")
    else:
        print("rejeita")
