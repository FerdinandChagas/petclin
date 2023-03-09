from core.entidades import *

cliente = Cliente()
cliente.nome='Ferdinandy'

dog = Animal()
dog.nome = 'Alfredo'
dog.idade = 7

atendimento = Atendimento()
atendimento.data= datetime.now()
atendimento.hora='10:00'
atendimento.animal= dog
atendimento.tutor = cliente


agenda = Agenda()
agenda.agendarConsulta(atendimento)
agenda.listarAgendamentos()

