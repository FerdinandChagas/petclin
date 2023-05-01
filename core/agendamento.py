from datetime import datetime
from typing import List
from .entidades import Atendimento, Medicamento


class Agendamento():
    """Classe responsavel pelos agendamentos"""

    def __init__(self):
        self.__agendamentos: List[Atendimento] = []  # lista de atendimentos
        self.__medicamentos: List[Medicamento] = []  # lista de

    def agendarConsulta(self, atendimento: Atendimento) -> bool:
        """Função responsavel por adicionar um agendamento"""
        date_atual = datetime.now()
        
        data_atual = '{}-{}-{}'.format(date_atual.year, date_atual.month if date_atual.month > 9 else str('0'+ str(date_atual.month)) , date_atual.day if date_atual.day > 9 else str('0'+ str(date_atual.day)))
        hora_atual = '{}:{}'.format(date_atual.hour, date_atual.minute
        )
        for  i in range(0, len(self.__agendamentos)):
            atendimento = self.__agendamentos[i]
            if atendimento.data == data_atual:
                if atendimento.hora == hora_atual:
                    raise ValueError ("Não é possivel realizar este agendamento, horario ocupado! Por favor, tente outro")
                
        self.__agendamentos.append(atendimento)
        return True

    def listarAgendamentos(self) -> List[Atendimento]:
        """Função responsavel por Listar os Agendamentos filtrando 
        por situação  """

        agendamentos = []
        for i in range(0, len(self.__agendamentos)):
            atendimento = self.__agendamentos[i]
            if atendimento.situacao == False:
                agendamentos.append(atendimento)

        return agendamentos

    def cancelarConsulta(self, atendimento: Atendimento) -> bool:
        """Função responsavel por cancelar um agendamento,
        filtrando por ID"""

        for i in range(0, len(self.__agendamentos)):
            ref = self.__agendamentos[i]
            if ref.id == atendimento.id:
                self.__agendamentos[i].situacao = True
                return True

        return False

    def adicionarPrescicao(self, medicamento: Medicamento) -> bool:
        """Função responsavel por adicionar uma prescrição de medicamento"""
        self.__medicamentos.append(medicamento)
        return True

    def obterPrescricoes(self) -> list:
        """Listando as prescrições de medicamento"""
        return self.__medicamentos

    def obterSolicitacoes(self) -> list: ...
    """ falta model de solicitação de exames"""
