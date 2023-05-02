from typing import List
import uuid


class Usuario:
    def __init__(self, nome: str, telefone: str, email: str, cpf: str, endereco: str, data_cadastro: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
        self.data_cadastro = data_cadastro
        self.id = None


class Funcionario(Usuario):
    def __init__(self, salario: float, funcao: str, horario: str, escala: str, login: str, senha: str, historico_ferias: list):
        super().__init__(nome='', telefone="", email="",
                         cpf="", endereco="", data_cadastro="")
        self.salario = salario
        self.funcao = funcao
        self.horario = horario
        self.escala = escala
        self.login = login
        self.senha = senha
        self.historico_ferias = historico_ferias  # list<ferias>


class Cliente(Usuario):
    def __init__(self, pets: list, caixa_msgs: list):
        super().__init__(nome='', telefone="", email="",
                         cpf="", endereco="", data_cadastro="")
        self.pets = pets  # list<animal>
        self.caixa_msgs = caixa_msgs  # list<string>

    def __str__(self) -> str:
        return str(
            {
                'nome': self.nome,
                'telefone': self.telefone,
                'email': self.email,
                'cpf': self.cpf,
                'endereco': self.endereco,
                'data_cadastro': self.data_cadastro,
                'animals': str([str(animal) for animal in self.pets])
            }
        )


class Animal:
    def __init__(self, nome: str, idade: int, raca: str, porte: str, vacinas: list, historico: list):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.vacinas = vacinas  # list<vacina>
        self.historico = historico  # list<atendimento>

    def __str__(self) -> str:
        return str({
            'nome': self.nome,
            'idade': self.idade,
            'raca': self.raca,
            'porte': self.porte,
            'vacinas': self.vacinas,
            'historico': [str (h) for h in self.historico]
        })


class Pagamento:
    def _init_(self, forma: str, parcelamento: int, valor: float, situacao: bool):
        self.forma = forma
        self.parcelamento = parcelamento
        self.valor = valor
        self.situacao = situacao


class Medicamento:
    def __init__(self, nome: str, fabricante: str, quantidade: int, validade: str, valor: float):
        self.nome = nome
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.validade = validade
        self.valor = valor


class Exame:
    def __init__(self, paciente: Animal, responsavel: Cliente, profissional: Funcionario, sintoma: str, dataExame: str, diagnostico: str, dataDiagnostico: str, medicacao: Medicamento, situacao: bool):
        self.paciente = paciente
        self.responsavel = responsavel
        self.profissional = profissional
        self.sintoma = sintoma
        self.dataExame = dataExame
        self.diagnostico = diagnostico
        self.dataDiagnostico = dataDiagnostico
        self.medicacao = medicacao
        self.situacao = situacao

    def __str__(self) -> str:
        return str('paciente: ' + self.paciente.__str__()) #falta fazer para todos os atts de medicamento

class Atendimento:
    def __init__(self, data: str, hora: str, animal: Animal, tutor: Cliente, motivo: str, tipo: str, pagamento: Pagamento, situacao: bool, exames: List[Exame]):
        self.data = data
        self.hora = hora
        self.animal = animal
        self.tutor = tutor
        self.motivo = motivo
        self.tipo = tipo
        self.pagamento = pagamento  # classe pagamento
        self.situacao = situacao
        self.exames = exames
        self.id = str(uuid.uuid4())

    def __str__(self) -> str:
        def str_tutor():
            return f"Nome: {self.tutor.nome} | CPF: {self.tutor.cpf} | Email: {self.tutor.email} | "

        def str_animal():
            return f"Nome: {self.animal.nome} | Idade: {self.animal.idade} | Raça: {self.animal.raca} | "

        def str_pagamento():
            return f"Forma: {self.pagamento.forma} | Parcelamento: {self.pagamento.parcelamento} | Valor: {self.pagamento.valor} | "
        return \
            f"data: {self.data} | hora: {self.hora} | " \
            + f"Motivo: {self.motivo} | Tipo: {self.tipo} | " \
            + f"Tutor: {str_tutor() if self.tutor else '-'} | " \
            + f"Animal: {str_animal() if self.animal else '-'} | " \
            + f"Pagamento: {str_pagamento() if self.pagamento else '-'} | " \
            + f"Situação: {'Ativo' if not self.situacao else 'Cancelado'}"



class Agenda:

    def __init__(self):
        self.agendamentos = []

    def agendarConsulta(self, atendimento):
        self.agendamentos.append(atendimento)

    def cancelarConsulta(self, cliente):
        pass

    def listarAgendamentos(self):
        for atendimento in self.agendamentos:
            print(
                f'{atendimento.data} - {atendimento.hora} - {atendimento.animal.nome} - {atendimento.tutor.nome}')
