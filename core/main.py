
class Pessoa:

    class Meta:
        nome=''
        cpf=''
        telefone=''
        endereco=''

class Animal:

    class Meta:
        tipo=''
        raca=''
        porte=''
        idade=0
        nome=''
        peso=1.0
        vacinas=[]


alfredo = Animal()
alfredo.tipo='cachorro'
alfredo.raca='Poodle'
alfredo.idade=8
alfredo.peso=7

dog=alfredo
dog.nome='alfredo'
print(dog.nome)
