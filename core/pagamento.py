# Inicializa uma lista vazia para armazenar o histórico de pagamentos
from core.entidades import Pagamento
from utils.print import clean


historico_de_pagamentos = []

# Define uma função para processar o pagamento


def processar_pagamento():
    clean()
    print("\n--- Dados para pagamento ---\n".upper())
    print("\ninforme um valor para pagamento: ".upper())
    valor = float(input())
    print("\ninforme a forma pagamento que deseja: ".upper())
    forma_pagamento = input()
    print("\ninforme a quantidade de parcelamento que deseja: ".upper())
    parcelamento = input()
    situacao = True
    # Simula o processamento do pagamento
    print("Processando pagamento de R$ {:.2f} com {} em {}x, situação: {}".format(
        valor, forma_pagamento, parcelamento, situacao))

    # Cria um dicionário com as informações do pagamento
    # pagamento = {"forma_pagamento": forma_pagamento, "parcelamento": parcelamento, "valor": valor, "situacao": situacao}

    # Adiciona o dicionário ao histórico de pagamentos realizados
    pagamento = Pagamento(
        forma=forma_pagamento, parcelamento=parcelamento, valor=valor, situacao=situacao)
    historico_de_pagamentos.append(
        pagamento
    )

    # Informa que o pagamento foi realizado com sucesso
    print("Pagamento de R$ {:.2f} com {} em {}x, situação: {} realizado com sucesso!".format(
        valor, forma_pagamento, parcelamento, situacao))
    return pagamento
# Define uma função para mostrar o histórico de pagamentos


def mostrar_historico_de_pagamentos():
    print("Histórico de pagamentos realizados:")
    for pagamento in historico_de_pagamentos:
        print(pagamento)


# Exemplo de uso das funções processar_pagamento e mostrar_historico_de_pagamentos
"""
processar_pagamento("cartão de crédito", 3, 150.0, True)
processar_pagamento("boleto", 1, 50.0, False)
"""

# mostrar_historico_de_pagamentos()
