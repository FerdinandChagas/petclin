class Animal:

    def __init__(self):
        self.nome=''
        self.idade=0
        self.raca=''
        self.porte=''
        self.vacinas=[]
        self.historico=[]
    
class Usuario:

    def __init__(self):
        self.nome=''
        self.telefone=''
        self.email=''
        self.cpf=''
        self.endereco=''
        self.data_cadastro=''

class Cliente(Usuario):

    def __init__(self):
        self.pet=Animal()

class Funcionario(Usuario):

    def __init__(self):
        self.salario=0.0
        self.funcao=''
        self.horario=''
        self.escala=''

class Atendimento:

    def __init__(self):
        self.data=''
        self.hora=''
        self.animal=Animal()
        self.tutor=Cliente()
        self.motivo=''

class Agenda:

    
    def __init__(self):
        self.agendamentos=[]
    
    def agendarConsulta(self, cliente, atendimento):
        pass

    def cancelarConsulta(self, cliente):
        pass

    def listarAgendamentos(self):
        for atendimento in self.agendamentos:
            print(f'{atendimento.data} - {atendimento.hora} - {atendimento.animal} - {atendimento.tutor}')