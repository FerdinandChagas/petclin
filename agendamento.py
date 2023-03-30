from typing import List
from entd import Atendimento, Cliente, Medicamento

class Agendamento():
    def __init__(self):
        self.__agendamentos: List[Atendimento] = [] #lista de atendimentos
        self.__medicamentos: List[Medicamento] = [] #lista de


    def agendarConsulta(self, atendimento:Atendimento)->bool: 
        self.__agendamentos.append(atendimento)
        return True
         


    def listarAgendamentos(self)->list:
        agendamentos = []
        for i in range(0, len(self.__agendamentos)):
            atendimento = self.__agendamentos[i] 
            if atendimento.situacao == False:
                agendamentos.append(atendimento)

        return agendamentos
       

    def cancelarConsulta(self, cliente: Cliente)->bool: 
        for i in range(0, len(self.__agendamentos)):
            atendimento = self.__agendamentos[i] 
            if atendimento.tutor.cpf == cliente.cpf:
                self.__agendamentos[i].situacao = True
                return True
        
        return False

    def adicionarPrescicao(self, medicamento:Medicamento)->bool: 
        self.__medicamentos.append(medicamento)
        return True
    
    def obterPrescricoes(self)->list:
        return self.__medicamentos

    def obterSolicitacoes(self)->list:...


    
