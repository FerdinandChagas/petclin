# Inicializa uma lista vazia para armazenar o histórico de pagamentos
historico_de_pagamentos = []

# Define uma função para processar o pagamento
def processar_pagamento(forma_pagamento, parcelamento, valor, situacao):
    # Simula o processamento do pagamento
    print("Processando pagamento de R$ {:.2f} com {} em {}x, situação: {}".format(valor, forma_pagamento, parcelamento, situacao))

    # Cria um dicionário com as informações do pagamento
    pagamento = {"forma_pagamento": forma_pagamento, "parcelamento": parcelamento, "valor": valor, "situacao": situacao}

    # Adiciona o dicionário ao histórico de pagamentos realizados
    historico_de_pagamentos.append(pagamento)

    # Informa que o pagamento foi realizado com sucesso
    print("Pagamento de R$ {:.2f} com {} em {}x, situação: {} realizado com sucesso!".format(valor, forma_pagamento, parcelamento, situacao))

# Define uma função para mostrar o histórico de pagamentos
def mostrar_historico_de_pagamentos():
    print("Histórico de pagamentos realizados:")
    for pagamento in historico_de_pagamentos:
        print("Forma de pagamento: {}, Parcelamento: {}x, Valor: R$ {:.2f}, Situação: {}".format(pagamento["forma_pagamento"], pagamento["parcelamento"], pagamento["valor"], pagamento["situacao"]))

# Exemplo de uso das funções processar_pagamento e mostrar_historico_de_pagamentos
"""
processar_pagamento("cartão de crédito", 3, 150.0, True)
processar_pagamento("boleto", 1, 50.0, False)
"""

mostrar_historico_de_pagamentos()
