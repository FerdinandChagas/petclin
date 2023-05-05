from datetime import datetime
from typing import Any, List
from .entidades import Atendimento, Exame, Medicamento


class Agendamento():
    """Classe responsavel pelos agendamentos"""

    def __init__(self):
        self.__agendamentos: List[Atendimento] = []  # lista de atendimentos

    def search_agendamento(self, id: str) -> Atendimento:
        for agendamento in self.__agendamentos:
            if agendamento.id == id:
                return agendamento
        return None

    def agendarConsulta(self, atendimento: Atendimento) -> bool:
        """Função responsavel por adicionar um agendamento"""
        date_atual = datetime.now()

        data_atual = '{}-{}-{}'.format(date_atual.year, date_atual.month if date_atual.month > 9 else str(
            '0' + str(date_atual.month)), date_atual.day if date_atual.day > 9 else str('0' + str(date_atual.day)))
        hora_atual = '{}:{}'.format(date_atual.hour, date_atual.minute
                                    )
        for i in range(0, len(self.__agendamentos)):
            ref = self.__agendamentos[i]
            if ref.data == data_atual:
                if ref.hora == hora_atual:
                    raise ValueError(
                        "Não é possivel realizar este agendamento, horario ocupado! Por favor, tente outro")

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

    def empty(self):
        return len(self.listarAgendamentos()) == 0

    def cancelarConsulta(self, atendimento: Atendimento) -> bool:
        """Função responsavel por cancelar um agendamento,
        filtrando por ID"""

        for i in range(0, len(self.__agendamentos)):
            ref = self.__agendamentos[i]
            if ref.id == atendimento.id:
                self.__agendamentos[i].situacao = True
                return True

        return False

    def adicionarPrescicao(self, variavel: Any, exame: Exame) -> bool:
        pass

    def adicionarPrescicao(self, variavel: Any, exame: Exame) -> bool:
        """Função responsavel por adicionar uma prescrição de medicamento"""
        if isinstance(variavel, str):
            agendamento = self.search_agendamento(variavel)
            if agendamento:
                agendamento.exames.append(exame)
                return True
            return False
        elif isinstance(variavel, Atendimento):
            variavel.exames.append(exame)
            return True

    def obterPrescricoes(self, variavel: Any) -> List[Medicamento]:
        """Listando as prescrições de medicamento"""
        if isinstance(variavel, str):
            agendamento = self.search_agendamento(variavel)
            if agendamento:
                return [e.medicacao for e in agendamento.exames]
        elif isinstance(variavel, Atendimento):
            return [e.medicacao for e in variavel.exames]
        return []

    def obterSolicitacoes(self, variavel: Any) -> List[Exame]:
        """Listando as solicitacoes de exames"""
        if isinstance(variavel, str):
            agendamento = self.search_agendamento(variavel)
            if agendamento:
                return agendamento.exames
        elif isinstance(variavel, Atendimento):
            return variavel.exames
        return []
