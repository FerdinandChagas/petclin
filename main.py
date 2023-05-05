from datetime import datetime
from core.agendamento import Agendamento
from core.entidades import Animal, Cliente, Medicamento, Funcionario, Exame, Atendimento
from core.pagamento import processar_pagamento
from utils.funcionario import get_funcionarios
from utils.medicamento import get_medicamentos
from utils.clients import get_clients
from utils.render import render_search
from utils.print import clean

clients = get_clients()
medicamentos = get_medicamentos()
funcionarios = get_funcionarios()
controle_agendamento = Agendamento()


def clients_search_by_id() -> Cliente:
    clean()
    return render_search("Clientes", clients)


def funcionarios_search_by_id() -> Funcionario:
    clean()
    return render_search("Profissionais", funcionarios)


def animals_search_by_id(client: Cliente) -> Animal:
    clean()
    return render_search("Animais", client.pets)


def medicamento_search_by_id() -> Medicamento:
    clean()
    return render_search("Medicamentos", medicamentos)


def add_exame(atendimento: Atendimento):
    if atendimento:
        clean()
        print("\n--- Dados para preenchimento Exame ---\n".upper())
        print("\nInforme a situação: ".upper())
        situacao = input()
        print("\nInforme a sintoma: ".upper())
        sintoma = input()
        print("\nInforme a Diagnóstico: ".upper())
        diagnostico = input()
        controle_agendamento.adicionarPrescicao(atendimento, Exame(medicacao=medicamento_search_by_id(), paciente=atendimento.animal, responsavel=atendimento.tutor, situacao=situacao, dataDiagnostico=str(
            datetime.now().date()), sintoma=sintoma, dataExame=str(datetime.now().date()), diagnostico=diagnostico, profissional=funcionarios_search_by_id()))


def render_agendamentos():

    def atendimento_search_by_id():
        clean()
        return render_search("Atendimentos", controle_agendamento.listarAgendamentos())

    while True:
        print("\n------------- Menu de Opções de agendamentos -------------".upper())
        print("------------- 1 - Realize um Agendamento -------------".upper())
        print("------------- 2 - Listar todos os Agendamentos -------------".upper())
        print("------------- 3 - Cancelar um Agendamento -------------".upper())
        print(
            "------------- 4 - Listar as Prescrições por agendamento -------------".upper())
        print("------------- 5 - Listar todas as Prescrições -------------".upper())
        print(
            "------------- 6 - Listar as Solicitações de Exames por agendamento -------------".upper())
        print(
            "------------- 7 - Listar todas as Solicitações de Exames -------------".upper())

        print("-------------          8 - Sair         -------------".upper())
        print("\ninforme sua entrada: ".upper())
        indice_menu = int(input())
        if indice_menu == 1:
            clean()
            try:
                print("\n--- Dados para preenchimento Atendimento ---\n".upper())
                data = datetime.now()
                hora = f'{data.hour}:{data.minute}'
                print("\ninforme um motivo: ".upper())
                result_input_motivo = input()
                print("\ninforme um tipo: ".upper())
                result_input_tipo = input()
                client = clients_search_by_id()
                animal = animals_search_by_id(client)
                atendimento = Atendimento(data=str(data.date()), hora=hora, animal=animal, tutor=client,
                                          motivo=result_input_motivo, tipo=result_input_tipo, pagamento=processar_pagamento(), situacao=False, exames=[])
                controle_agendamento.agendarConsulta(atendimento)
                animal.historico.append(atendimento)
                add_exame(atendimento=atendimento)
                clean()
            except ValueError as e:
                print(e)
        elif indice_menu == 2:
            clean()
            if controle_agendamento.empty():
                print("\nSem atendimentos\n".upper())
            else:
                for a in controle_agendamento.listarAgendamentos():
                    print(a)
        elif indice_menu == 3:
            clean()
            if controle_agendamento.empty():
                print("\nSem atendimentos\n".upper())
            else:
                controle_agendamento.cancelarConsulta(
                    atendimento_search_by_id())
                clean()
        elif indice_menu == 4:
            clean()
            if controle_agendamento.empty():
                print("\nSem Prescrições\n".upper())
            else:
                for medicamento in controle_agendamento.obterPrescricoes(
                        atendimento_search_by_id()):
                    print(medicamento)
        elif indice_menu == 5:
            clean()
            if controle_agendamento.empty():
                print("\nSem Prescrições\n".upper())
            else:
                for atendimento in controle_agendamento.listarAgendamentos():
                    for medicamento in controle_agendamento.obterPrescricoes(atendimento):
                        print(medicamento)
        elif indice_menu == 6:
            clean()
            if controle_agendamento.empty():
                print("\nSem Solicitações\n".upper())
            else:
                for solicitacao in controle_agendamento.obterSolicitacoes(atendimento_search_by_id()):
                    print(solicitacao)

        elif indice_menu == 7:
            clean()
            if controle_agendamento.empty():
                print("\nSem Solicitações\n".upper())
            else:
                for atendimento in controle_agendamento.listarAgendamentos():
                    for exame in controle_agendamento.obterSolicitacoes(atendimento):
                        print(exame)
        elif indice_menu == 8:
            break


render_agendamentos()

# print([str(c) for c in get_clients()])
