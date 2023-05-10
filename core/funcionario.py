from utils.print import clean
from .entidades import Funcionario, PontoFuncionario

def add_funcionarios(funcionario: Funcionario):
    if funcionario:
        clean()
        print ("Ponto do funcionario adicionado com sucesso!")
        funcionario.pontos.append(PontoFuncionario())
