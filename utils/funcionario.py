
from datetime import datetime
from typing import List
from core.entidades import Funcionario
from utils.random import get_name
from utils.clients import get_cpf, get_email, get_endereco, get_name, get_phone


def get_funcionarios() -> List[Funcionario]:
    funcionarios = []

    for _ in range(0, 10):
        funcionario = Funcionario(funcao='Veterinária', escala='', historico_ferias=[
        ], horario='8h ás 12h', login='', senha='123', salario=3000, pontos=[])
        funcionario.nome = get_name().capitalize()
        funcionario.telefone = get_phone()
        funcionario.cpf = get_cpf()
        funcionario.data_cadastro = str(datetime.now().date())
        funcionario.email = get_email(funcionario.nome.lower())
        funcionario.login = funcionario.email
        funcionario.endereco = get_endereco()
        funcionarios.append(funcionario)

    return funcionarios
