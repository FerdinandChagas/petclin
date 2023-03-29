class Usuario:
    def __init__(self, nome: str, telefone: str, email: str, cpf: str, endereco: str, data_cadastro: str):
        self.nome = ''
        self.telefone = ''
        self.email = ''
        self.cpf = ''
        self.endereco = ''
        self.data_cadastro = ''


class Funcionario(Usuario):
    def __init__(self, salario: float, funcao: str, horario: str, escala: str, login: str, senha: str, historico_ferias: list):
        self.salario = 0.0
        self.funcao = ''
        self.horario = ''
        self.escala = ''
        self.login = ''
        self.senha = ''
        self.historico_ferias = []  # list<ferias>


class Cliente(Usuario):
    def __init__(self, pets: list, caixa_msgs: list):
        self.pets = []  # list<animal>
        self.caixa_msgs = []  # list<string>


class Animal:
    def __init__(self, nome: str, idade: int, raca: str, porte: str, vacinas: list, historico: list):
        self.nome = ''
        self.idade = 0
        self.raca = ''
        self.porte = ''
        self.vacinas = []  # list<vacina>
        self.historico = []  # list<atendimento>


class Pagamento:
    def _init_(self, forma: str, parcelamento: int, valor: float):
        self.forma = ''
        self.parcelamento = 1
        self.valor = 0.0


class Atendimento:
    def __init__(self, data: str, hora: str, animal: Animal, tutor: Cliente, motivo: str, tipo: str, pagamento: Pagamento):
        self.data = ''
        self.hora = ''
        self.animal = Animal
        self.tutor = Cliente
        self.motivo = ''
        self.tipo = ''
        self.pagamento = Pagamento()  # classe pagamento
