
from datetime import datetime
from typing import List
from core.entidades import Cliente
from utils.animals import get_animals
from utils.random import random, numbers, get_name


dominios = ['@gmail.com', '@hotmail.com', '@outlook.com.br', '@outlook.com']


def get_phone():
    value = ""
    for i in range(0, 12):
        rand = str(random(array=numbers))
        if i == 0:
            value += f'({rand}'
        elif i == 1:
            value += f'{rand}) '
        elif i == 7:
            value += '-'
        else:
            value += rand
    return value


def get_endereco():
    return f"Rua {get_name().capitalize()} Nº {random(array=numbers)}"


def get_cpf():
    value = ""
    for i in range(0, 11):
        rand = str(random(array=numbers))
        if i == 2:
            value += f'{rand}.'
        elif i == 6:
            value += f'.{rand}'
        elif i == 8:
            value += f'{rand}-'
        else:
            value += rand
    return value


def get_email(value: str):
    return f"{value.replace(' ', '_')}{random(dominios)}"


def get_clients() -> List[Cliente]:
    clients = []

    for _ in range(0, 3):
        client = Cliente(get_animals(), [])
        client.nome = get_name().capitalize()
        client.telefone = get_phone()
        client.cpf = get_cpf()
        client.data_cadastro = str(datetime.now().date())
        client.email = get_email(client.nome.lower())
        client.endereco = get_endereco()
        clients.append(client)

    return clients
