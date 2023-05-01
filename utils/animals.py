from core.entidades import Animal
from utils.random import get_name, get_number, random

names_animals = ['Akita', 'Basset hound', 'Beagle', 'Bichon frisé', 'Boiadeiro australiano', 'Border collie', 'Boston terrier', 'Boxer', 'Buldogue francês', 'Buldogue inglês', 'Bull terrier', 'Cane corso', 'Cavalier king charles spaniel', 'Chihuahua', 'Chow chow', 'Cocker spaniel inglês', 'Dachshund', 'Dálmata', 'Doberman', 'Dogo argentino', 'Dogue alemão', 'Fila brasileiro', 'Golden retriever',
                 'Husky siberiano', 'Jack russell terrier', 'Labrador retriever', 'Lhasa apso', 'Lulu da pomerânia', 'Maltês', 'Mastiff inglês', 'Mastim tibetano', 'Pastor alemão', 'Pastor australiano', 'Pastor de Shetland', 'Pequinês', 'Pinscher', 'Pit bull', 'Poodle', 'Pug', 'Rottweiler', 'Schnauzer', 'Shar-pei', 'Shiba', 'Shih tzu', 'Staffordshire bull terrier', 'Weimaraner', 'Yorkshire']


def get_animals():
    animals = []

    for _ in range(0, 1):
        animals.append(Animal(nome=get_name(), idade=get_number(), raca=random(
            names_animals), porte='', vacinas=[], historico=[]))

    return animals
