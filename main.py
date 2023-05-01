from datetime import datetime
from core.agendamento import Agendamento
from core.entidades import Animal, Cliente
from core.entidades import Atendimento
from utils.clients import get_clients

clients = get_clients()


def clients_search_by_id() -> Cliente:
    size = len(clients)
    print("------------- Clientes -------------")
    print("------------- Busque por index -------------")
    for index in range(0, size):
        print(f"{index}- {clients[index].nome}")
    indice_menu = int(input())
    if indice_menu < 0 or indice_menu > size:
        print("informe um indice valido")
        return clients_search_by_id()
    return clients[indice_menu]


def animals_search_by_id(client: Cliente) -> Animal:
    animals = client.pets
    size = len(animals)
    print("------------- Animais -------------")
    print("------------- Busque por index -------------")
    for index in range(0, size):
        print(f"{index}- {animals[index].nome}")
    indice_menu = int(input())
    if indice_menu < 0 or indice_menu > size:
        print("informe um indice valido")
        return animals_search_by_id()
    return animals[indice_menu]


def render_agendamentos():

    controle_agendamento = Agendamento()

    def atendimento_search_by_id():
        atendimentos = controle_agendamento.listarAgendamentos()
        size = len(atendimentos)
        print("------------- Listar dos atendimentos -------------")
        print("------------- Busque por index -------------")
        for index in range(0, size):
            atendimento = atendimentos[index]
            print(f"{index}- {atendimento.motivo} | {atendimento.tipo}")
        indice_menu = int(input())
        if indice_menu < 0 or indice_menu > size:
            print("informe um indice valido")
            return atendimento_search_by_id()
        return atendimentos[indice_menu]

    while True:
        print("-------------Menu de Opções de agendamentos-------------")
        print("-------------1 - Realize um Agendamento -------------")
        print("-------------2 - Listar todos os Agendamentos -------------")
        print("-------------3 - Cancelar um Agendamento -------------")
        print("-------------4 - Realize uma prescrição -------------")
        print("-------------5 - Listar todas as Prescrições -------------")
        print("-------------          6 - Sair         -------------")
        indice_menu = int(input())
        if indice_menu == 1:
            try:
                data = datetime.now()
                hora = f'{data.hour}:{data.minute}'
                print("informe um motivo")
                result_input = input()
                print("informe um tipo")
                result_input_tipo = input()
                client = clients_search_by_id()
                animal = animals_search_by_id(client)
                atendimento = Atendimento(data=str(data.date()), hora=hora, animal=animal, tutor=client,
                                        motivo=result_input, tipo=result_input_tipo, pagamento=None, situacao=False)
                animal.historico.append(atendimento)
                controle_agendamento.agendarConsulta(atendimento)
            except ValueError as e:
                print(e)
        elif indice_menu == 2:
            for a in controle_agendamento.listarAgendamentos():
                print(a)
        elif indice_menu == 3:
            controle_agendamento.cancelarConsulta(atendimento_search_by_id())
            # Falta as opções do controle de usuario pra buscarmos o cliente
        elif indice_menu == 4:
            controle_agendamento.adicionarPrescicao()
        elif indice_menu == 5:
            controle_agendamento.obterPrescricoes()
        elif indice_menu == 6:
            break


render_agendamentos()

# print([str(c) for c in get_clients()])
