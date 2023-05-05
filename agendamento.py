from typing import List
from entd import Atendimento, Cliente, Medicamento


class Agendamento:
    """Classe responsavel pelos agendamentos"""

    def __init__(self):
        self.__agendamentos: List[Atendimento] = []  # lista de atendimentos
        self.__medicamentos: List[Medicamento] = []  # lista de

    def agendarConsulta(self, atendimento: Atendimento) -> bool:
        """Função responsavel por adicionar um agendamento"""

        self.__agendamentos.append(atendimento)
        return True

    def listarAgendamentos(self) -> list:
        """Função responsavel por Listar os Agendamentos filtrando 
        por situação  """

        agendamentos = []
        for i in range(0, len(self.__agendamentos)):
            atendimento = self.__agendamentos[i]
            if atendimento.situacao == False:
                agendamentos.append(atendimento)

        return agendamentos

    def cancelarConsulta(self, cpf: str, nomeAnimal: str) -> bool:
        """Função responsavel por cancelar um agendamento,
        filtrando por CPF"""

        for i in range(0, len(self.__agendamentos)):
            atendimento = self.__agendamentos[i]
            if atendimento.tutor.cpf == cpf and atendimento.animal.nome:
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

    def obterSolicitacoes(self) -> list:
        ...

    """ falta model de solicitação de exames"""
