import os


def clean():
    os.system('clear')


def str_user(self):
    return f"Nome: {self.nome} \t Telefone: {self.telefone} \t E-mail: {self.email} \t Cpf: {self.cpf}\tEndereço: {self.endereco} \tData Cadastro: {self.data_cadastro}\n"
