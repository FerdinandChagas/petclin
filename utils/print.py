import os
""" funções usadas para limpar o terminal e printar as informações"""

def clean():
    os.system('cls')


def str_user(self):
    return f"Nome: {self.nome} \t Telefone: {self.telefone} \t E-mail: {self.email} \t Cpf: {self.cpf}\tEndereço: {self.endereco} \tData Cadastro: {self.data_cadastro}\n"
