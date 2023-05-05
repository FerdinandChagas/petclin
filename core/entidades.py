from typing import List
import uuid
from utils.print import str_user


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

    def __str__(self) -> str:
        return f"{str_user(self)}Salario: {self.salario}\tFunção: {self.funcao}\tHorário: {self.horario}\tEscala: {self.escala}\nLogin: {self.login}\tSenha: {self.senha}\n"


class Cliente(Usuario):
    def __init__(self, pets: list, caixa_msgs: list):
        super().__init__(nome='', telefone="", email="",
                         cpf="", endereco="", data_cadastro="")
        self.pets = pets  # list<animal>
        self.caixa_msgs = caixa_msgs  # list<string>

    def __str__(self) -> str:
        _str_animals = ""
        for p in self.pets:
            _str_animals += f"{p}\n"
        return f"{str_user(self)}Animals:\n{_str_animals}\n"


class Animal:
    def __init__(self, nome: str, idade: int, raca: str, porte: str, vacinas: list, historico: list):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.vacinas = vacinas  # list<vacina>
        self.historico = historico  # list<atendimento>

    def __str__(self) -> str:
        _str_historico = ""
        for h in self.historico:
            _str_historico += f"{h}\n"
        return f"Nome: {self.nome} \t Idade: {self.idade} \t Raça: {self.raca} \t Porte: {self.porte}\nHistorico:\n{_str_historico}"


class Pagamento:
    def __init__(self, forma: str, parcelamento: int, valor: float, situacao: bool):
        self.forma = forma
        self.parcelamento = parcelamento
        self.valor = valor
        self.situacao = situacao

    def __str__(self) -> str:
        return "Forma: {} \t Valor: {} \t Parcelamento: {}\t Situação: {}".format(self.valor, self.forma_pagamento, self.parcelamento, self.situacao)


class Medicamento:
    def __init__(self, nome: str, fabricante: str, quantidade: int, validade: str, valor: float):
        self.nome = nome
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.validade = validade
        self.valor = valor

    def __str__(self) -> str:
        return f"Nome: {self.nome} \tFabricante: {self.fabricante}\tQuantidade: {self.quantidade}\tValidade: {self.validade}\tValor: {self.valor}"


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
        # falta fazer para todos os atts de medicamento
        _str_desc = "\n\n------ Dados Exame ------\n\n".upper()
        return str(f"{_str_desc}\nSintoma: {self.sintoma} \t Data Exame: {self.dataExame} \nDiagnóstico: {self.diagnostico} \t Data Diagnóstico: {self.dataDiagnostico} \n\nProfissional: \n{self.profissional.__str__()}\n\nPaciente:\n {self.paciente.__str__()}\n\n ")


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
            return f"Nome: {self.tutor.nome} \t CPF: {self.tutor.cpf} \t Email: {self.tutor.email}\n"

        def str_animal():
            return f"Nome: {self.animal.nome} \t Idade: {self.animal.idade} \t Raça: {self.animal.raca} \n"

        def str_pagamento():
            return f"Forma: {self.pagamento.forma} \t Parcelamento: {self.pagamento.parcelamento} \t Valor: {self.pagamento.valor} \n"
        _str_tutor = str_tutor() if self.tutor else '-'
        _str_animal = str_animal() if self.animal else '-'
        _str_pagamento = str_pagamento() if self.pagamento else '-'
        _str_desc = "\n\n------ Dados Atendimento ------\n\n".upper()
        return f"{_str_desc}Data: {self.data}\tHora: {self.hora}\tMotivo: {self.motivo}\tTipo: {self.tipo}\n\nTutor:\n{_str_tutor}\nAnimal: \n{_str_animal}\nPagamento: \n{_str_pagamento}\nSituação: {'Ativo' if not self.situacao else 'Cancelado'}".upper() + '\n\n'
