from core.entidades import *

cliente = Cliente()
cliente.nome='Ferdinandy'

dog = Animal()
dog.nome = 'Alfredo'
dog.idade = 7

atendimento = Atendimento()
atendimento.data='10/03/2023'
atendimento.hora='10:00'
atendimento.animal= dog
atendimento.tutor = cliente


agenda = Agenda()
agenda.agendarConsulta(atendimento)
agenda.listarAgendamentos()

