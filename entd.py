class Usuario:
    def __init__(self, nome: str, telefone: str, email: str, cpf: str, endereco: str, data_cadastro: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
        self.data_cadastro = data_cadastro

class Funcionario(Usuario):
    def __init__(self, salario: float, funcao: str, horario: str, escala: str, login: str, senha: str, historico_ferias: list):
        super().__init__(nome='', telefone="", email="", cpf="", endereco="", data_cadastro="")
        self.salario = salario
        self.funcao = funcao
        self.horario = horario
        self.escala = escala
        self.login = login
        self.senha = senha    
        self.historico_ferias = historico_ferias  # list<ferias>

class Cliente(Usuario):
    def __init__(self, pets: list, caixa_msgs: list):
        super().__init__(nome='', telefone="", email="", cpf="", endereco="", data_cadastro="")
        self.pets = pets  # list<animal>
        self.caixa_msgs = caixa_msgs  # list<string>

class Animal:
    def __init__(self, nome: str, idade: int, raca: str, porte: str, vacinas: list, historico: list):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.vacinas = vacinas  # list<vacina>
        self.historico = historico  # list<atendimento>

class Pagamento:
    def _init_(self, forma: str, parcelamento: int, valor: float, situacao: bool):
        self.forma = forma
        self.parcelamento = parcelamento
        self.valor = valor
        self.situacao = situacao

class Atendimento:
    def __init__(self, data: str, hora: str, animal: Animal, tutor: Cliente, motivo: str, tipo: str, pagamento: Pagamento, situacao: bool):
        self.data = data
        self.hora = hora
        self.animal = animal
        self.tutor = tutor
        self.motivo = motivo
        self.tipo = tipo
        self.pagamento = pagamento  # classe pagamento
        self.situacao = situacao
   
    def _str_(self) -> str:
        def str_tutor(): 
            return f"Nome: {self.tutor.nome}\tCPF: {self.tutor.cpf}\tEmail: {self.tutor.email}\t"  
        def str_animal():
            return f"Nome: {self.animal.nome}\tIdade: {self.animal.idade}\Raça: {self.animal.raca}\t" 
        def str_pagamento():
            return f"Forma: {self.pagamento.forma}\tParcelamento: {self.pagamento.parcelamento}\Valor: {self.pagamento.valor}\t"
        return \
        f"data: {self.data}\thora: {self.hora}\n" \
        + f"Motivo: {self.motivo}\tTipo: {self.tipo}\n" \
        + f"Tutor: {str_tutor() if self.tutor else '-'}\n" \
        + f"Animal: {str_animal() if self.animal else '-'}\n" \
        + f"Pagamento: {str_pagamento() if self.pagamento else '-'}\n" \
        + f"Situação: {'Ativo' if self.situacao else 'Cancelado'}"

class Medicamento:
    def __init__(self, nome: str, fabricante: str, quantidade: int, validade: str, valor: float):
        self.nome = nome
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.validade = validade
        self.valor = valor
