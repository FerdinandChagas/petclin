
class Pessoa:

    class Meta:
        nome=''
        cpf=''
        telefone=''
        endereco=''
        

class Cliente(Pessoa):
    
    class Meta:
        histpay=[]

class Funcionario(Pessoa):

    class Meta:
        salario=0.0
        funcao=''
        data_entrada=''
        data_saida=''

class Animal:

    class Meta:
        tipo=''
        raca=''
        porte=''
        idade=0
        nome=''
        peso=1.0
        vacinas=[]
        tutor= Pessoa()

class Servico:

    class Meta:
        descricao=''
        valor=''

class Agenda:

    class Meta:
        data=''
        cliente= Animal()
        servicos= Servico[]

    def agendar(cliente,servicos,data):
        agenda_geral.append()


class Venda:

    def realizarPagamento(itens, cliente, tipo_pagamento):
        if pagar(itens.total, tipo_pagamento):
            cliente.histpay.append(itens,data)

    
