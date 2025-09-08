def op_negacao(valor):
    return not valor

def op_conjuncao(valor_1, valor_2):
    return valor_1 and valor_2

def op_disjuncao(valor_1, valor_2):
    return valor_1 or valor_2

def op_implicacao(valor_1, valor_2):
    return not valor_1 or valor_2

def op_bicondicional(valor_1, valor_2):
    return valor_1 == valor_2

def atrib_valores_logicos():
    p = [True, True, False, False]
    q = [True, False, True, False]
    return p, q

def neg_valores_logicos():
    nao_p = [False, False, True, True]
    nao_q = [False, True, False, True]
    return nao_p, nao_q

def normal_caracteres(proposicao):
    for i in range (len(proposicao)):
        if proposicao[i] == '^' or proposicao[i] == '^' or proposicao[i] == 'ˆ':
            operador == op_and
        elif proposicao[i].lower() == 'v' or proposicao[i] == 'ˇ':
            operador == op_or
        elif proposicao[i] == '-':
            if proposicao[i+1] == '>':
                operador == op_imp
        elif proposicao[i] == '<':
            if proposicao[i+1] == '-':
                if proposicao[i+2] == '>':
                    operador == op_bicond
        else:
            return None

def extrair_operador(proposicao):
    i = 0
    while i < len(proposicao):
        if i + 2 < len(proposicao) and proposicao[i:i+3] == "<->":
            operador = op_bicond
            esquerda = proposicao[:i]
            direita = proposicao[i+3:]
            return esquerda, operador, direita
        elif i + 1 < len(proposicao) and proposicao[i:i+2] == "->":
            operador = op_imp
            esquerda = proposicao[:i]
            direita = proposicao[i+2:]
            return esquerda, operador, direita
        elif proposicao[i] == "^":
            operador = op_and
            esquerda = proposicao[:i]
            direita = proposicao[i+1:]
            return esquerda, operador, direita
        elif proposicao[i] == "v":
            operador = op_or
            esquerda = proposicao[:i]
            direita = proposicao[i+1:]
            return esquerda, operador, direita
        i += 1

    return "Formato inválido!!!"
