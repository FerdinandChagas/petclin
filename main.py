from datetime import datetime
from agendamento import Agendamento
from entd import Atendimento

def render_agendamentos():

    controle_agendamento = Agendamento()

    while True: 
        print("-------------Menu de Opções de agendamentos-------------")
        print("-------------1- Realize um Agendamento -------------")
        print("-------------2 - Listar todos os Agendamentos-------------")
        print("-------------3 - Cancelar um Agendamento -------------")
        print("-------------4 - Realize uma prescrição -------------")
        print("-------------5 - Listar todas as Prescrições -------------")
        print("-------------          6 - Sair         -------------")
        indice_menu = int(input())
        if indice_menu == 1:
            data = datetime.now()
            hora = f'{data.hour}:{data.minute}:{data.second}'
            print("informe um motivo")
            result_input = input()
            print("informe um tipo")
            result_input_tipo = input()
            atendimento = Atendimento(data=str(data.date()),hora=hora, animal=None, tutor=None, motivo=result_input, tipo=result_input_tipo, pagamento=None )
            controle_agendamento.agendarConsulta(atendimento)
        elif indice_menu == 2:
            print([str(a) for a in controle_agendamento.listarAgendamentos()])
        elif indice_menu == 3:
            controle_agendamento.cancelarConsulta()
            #Falta as opções do controle de usuario pra buscarmos o cliente
        elif indice_menu == 4:
            controle_agendamento.adicionarPrescicao()
        elif indice_menu == 5:
            controle_agendamento.obterPrescricoes()
        elif indice_menu == 6:
            break
 
render_agendamentos()

