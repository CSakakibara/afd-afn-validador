numero_de_estados = int(input()) #Linha 1: numero de estados n
conjunto_de_estados = set(str(i) for i in range(numero_de_estados)) #Criando um conjunto com os estados
conjunto_de_simbolos_terminais = input().split() #Linha 2: conjunto de simbolos terminais (lista)
conjunto_de_estados_de_aceitacao = input().split() #Linha 3: conjunto de estados de aceitacao (lista)
numero_de_transicoes_do_automato = int(input()) #Linha 4: numero t de transicoes (inteiro)

conjunto_de_simbolos_terminais = conjunto_de_simbolos_terminais[slice(1, int(conjunto_de_simbolos_terminais[0]) + 1)] #Removendo o primeiro elemento(quantidade)

conjunto_de_estados_de_aceitacao = set(conjunto_de_estados_de_aceitacao[slice(1, int(conjunto_de_estados_de_aceitacao[0]) + 1)]) #Removendo o primeiro elemento e criando conjunto

conjunto_de_transicoes = {} #Criando conjunto de transicoes
for estado in conjunto_de_estados: #Para cada estado, preencher o conjunto de transicoes com uma chave de cada simbolo do alfabeto, basicamente criando uma tabela imaginaria com todas as possibilidades (ainda sem os valores)
    conjunto_de_transicoes[estado] = {simbolo: set() for simbolo in conjunto_de_simbolos_terminais}

for i in range(numero_de_transicoes_do_automato): #Receber de acordo com o numero de transicoes
    transicao_i = input().split() #A partir da Linha 5, sao fornecidas todas as t transicoes
    conjunto_de_transicoes[transicao_i[0]][transicao_i[1]].add(transicao_i[2]) #Preencher o conjunto de transicoes com o valor(estado destino)

#Fazer equivalencia deterministica pra automato nao deterministico
estados_de_aceitacao_deterministico = set() #Conjunto pra armazenar os novos estados de aceitacao
transicoes_deterministico = {} #Armazenar as novas transicoes

analisar_para_equivalencia = [set('0')] #Inicializando com o estado inicial

while len(analisar_para_equivalencia) > 0:
    proximo_estado = analisar_para_equivalencia.pop(0) #Pegar e remover o primeiro elemento da fila
    qual_proximo_estado = "".join([str(i) for i in proximo_estado]) #Indice
    if conjunto_de_estados_de_aceitacao.intersection(proximo_estado):
        estados_de_aceitacao_deterministico.add(qual_proximo_estado) #Incluindo nos novos estados de aceitacao

    transicoes_deterministico[qual_proximo_estado] = {simbolo: None for simbolo in conjunto_de_simbolos_terminais} #Em cada estado criar a estrutura das possibilidades pra cada simbolo

    for simbolo in conjunto_de_simbolos_terminais:
        estados_destino = []
        for estado in proximo_estado:
            for transicao in conjunto_de_transicoes[estado][simbolo]:
                if transicao not in estados_destino:
                    estados_destino.append(transicao) #Armazenar as possiveis transicoes com o simbolo
        estado_destino = "".join([str(i) for i in estados_destino]) #Concatenar pra dar nome ao novo estado
        transicoes_deterministico[qual_proximo_estado][simbolo] = estado_destino #Preencher a "tabela" de possibilidades com o valor
        if estado_destino not in transicoes_deterministico:
            analisar_para_equivalencia.append(estados_destino) #Adicionar novo estado na iteracao

#Tratar as cadeias
numero_de_cadeias = int(input()) #Depois das t transicoes, na linha seguinte e dado o numero c de cadeias de entrada que serao avaliadas
for i in range(numero_de_cadeias):
    cadeia = input() #Nas proximas c linhas serao fornecidas as cadeias de entrada (uma por linha)
    proximo_estado = "0" #Inicializando com o estado inicial
    if cadeia == '-' and proximo_estado in estados_de_aceitacao_deterministico: #Caso da cadeia vazia
        print('aceita')
    else:
        nao_acabou = True
        for simbolo in cadeia: #Caso em que haja simbolo que nao faz parte do alfabeto
            if simbolo not in conjunto_de_simbolos_terminais:
                print('rejeita')
                nao_acabou = False
                break
            else:
                proximo_estado = transicoes_deterministico[proximo_estado][simbolo]
                if proximo_estado is None: #Caso em que transicao nao esteja definida
                    print('rejeita')
                    nao_acabou = False
                    break
        if nao_acabou: #Casos normais
            if proximo_estado in estados_de_aceitacao_deterministico:
                print('aceita')
            else:
                print('rejeita')
