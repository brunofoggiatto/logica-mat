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

def normal_caracteres(caractere_ou_operador):
    caractere_ou_operador = caractere_ou_operador.lower()
    
    if caractere_ou_operador in ['ˆ', '^','&']:
        return "op_conjuncao"
    elif caractere_ou_operador in ['v', 'ˇ','|']:
        return "op_disjuncao"
    elif caractere_ou_operador in ['->', '-->','>']:
        return "op_implicacao"
    elif caractere_ou_operador in ['<->', '<-->','<>']:
        return "op_bicondicional"
    else:
        return None

def extrair_operador(proposicao):
    operador = ""
    esquerda = ""
    direita = ""

    i = 0
    while i < len(proposicao):
        if i + 2 < len(proposicao) and proposicao[i:i+3] == "<->":
            operador = "op_bicondicional"
            esquerda = proposicao[:i]
            direita = proposicao[i+3:]
            return esquerda, operador, direita
        elif i + 1 < len(proposicao) and proposicao[i:i+2] == "->":
            operador = "op_implicacao"
            esquerda = proposicao[:i]
            direita = proposicao[i+2:]
            return esquerda, operador, direita
        elif proposicao[i] == "^":
            operador = "op_conjuncao"
            esquerda = proposicao[:i]
            direita = proposicao[i+1:]
            return esquerda, operador, direita
        elif proposicao[i] == "v":
            operador = "op_disjuncao"
            esquerda = proposicao[:i]
            direita = proposicao[i+1:]
            return esquerda, operador, direita
        i += 1
    
    print("Formato inválido!!!")
    return None, None, None

def tabela_verdade(proposicao):
    p, q = atrib_valores_logicos()
    nao_p, nao_q = neg_valores_logicos()
    
    proposicao = proposicao.replace(" ", "")
    
    esquerda, operador, direita = extrair_operador(proposicao)
    
    if operador is None:
        return

    operacoes = {
        "op_conjuncao": op_conjuncao,
        "op_disjuncao": op_disjuncao,
        "op_implicacao": op_implicacao,
        "op_bicondicional": op_bicondicional
    }
    
    func = operacoes.get(operador)
    
    if func is None:
        print("Proposição inválida!!!")
        return

    print(f"{'p':^5} {'q':^5} {'¬p':^5} {'¬q':^5} {proposicao:^8}")
    print("-" * 40)

    for i in range(4):
        val_esquerda = p[i] if esquerda == 'p' else q[i] if esquerda == 'q' else None
        val_direita = p[i] if direita == 'p' else q[i] if direita == 'q' else None
        
        resultado = func(val_esquerda, val_direita)
        
        p_str = "V" if p[i] else "F"
        q_str = "V" if q[i] else "F"
        nao_p_str = "V" if nao_p[i] else "F"
        nao_q_str = "V" if nao_q[i] else "F"
        resultado_str = "V" if resultado else "F"
        
        print(f"{p_str:^5} {q_str:^5} {nao_p_str:^5} {nao_q_str:^5} {resultado_str:^8}")

def executar():
    while True:
        entrada = input("Digite a proposição (ou 'sair'): ")
        if entrada.lower() == 'sair':
            print("Encerrando...")
            break
        elif entrada.strip():
            tabela_verdade(entrada)
        print()

if __name__ == "__main__":
    executar()
