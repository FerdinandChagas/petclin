from datetime import datetime
from agendamento import Agendamento
from entd import Atendimento, Animal, Cliente


def render_agendamentos():

    controle_agendamento = Agendamento()
    # Lista de clientes cadastrados no sistema
    clientes = list()
    # Lista de Animais cadastrados no sistema
    animais = list()

    while True: 
        print("-------------Menu de Opções de agendamentos-------------")
        print("-------------1 - Realize um Agendamento    -------------")
        print("-------------2 - Listar todos os Agendamentos-----------")
        print("-------------3 - Cancelar um Agendamento   -------------")
        print("-------------4 - Listar clientes e animais -------------")
        print("-------------5 - Realize uma prescrição    -------------")
        print("-------------6 - Listar todas as Prescrições -----------")
        print("-------------7 - Sair                      -------------")
        print("Digite uma opção: ")
        indice_menu = int(input())
        if indice_menu == 1:
            data = datetime.now()
            hora = f'{data.hour}:{data.minute}:{data.second}'
            print("informe um motivo: ")
            result_input = input()
            print("informe um tipo:")
            result_input_tipo = input()
            # Recebe os dados do animal
            nomeAnimal = input("Informe o nome do Animal: ")
            idadeAnimal = input("Informe a idade do animal: ")
            racaAnimal = input("Informe a raça do animal: ")
            porteAnimal = input("Informe o porte do animal(Grande-Medio-Pequeno):")
            vac = ' '
            listVac = list()

            # Cria uma entidade animal com os atributos dados
            animal = Animal(nomeAnimal, idadeAnimal, racaAnimal, porteAnimal, listVac)
            # Verifica se o animal ja esta cadastrado
            if len(animais) != 0:
                cad = False
                for anim in animais:
                    if anim.nome == animal.nome and anim.idade == animal.idade and anim.raca == animal.raca:
                        if anim.porte == animal.porte:
                            animal = anim
                            cad = True
                            break
                if not cad:
                    # Caso não esteja vazia, mas o animal nao esteja cadastrado, ele é cadastrado na lista
                    while vac != 0:
                        vac = input("Informe a vacina(Digite '0' para terminar de preencher a lista): ")
                        if vac == "0":
                            break
                        listVac.append(vac)
                    animais.append(animal)
            else:
                # Caso esteja vazia termina de preecher os dados do animal e o cadastra na lista
                while vac != 0:
                    vac = input("Informe a vacina(Digite '0' para terminar de preencher a lista): ")
                    if vac == "0":
                        break
                    listVac.append(vac)
                animais.append(animal)
            # Recebe o CPF
            cpf = input("Informe o cpf do cliente: ")

            # Verifica se ha cadastros no sistema, e apos se o cpf esta cadastrado no sistema
            if len(clientes) != 0:
                for clien in clientes:
                    if clien.cpf == cpf:
                        tutor = clien
            else:
                # Caso não esteja, entao o cliente sera cadastrado
                nomeCliente = input("Informe o nome do cliente: ")
                telefone = input("Informe o telefone: ")
                email = input("Informe o e-mail do cliente")
                endereco = input("Informe o endereço do cliente: ")
                pets = list()
                pets.append(animal)
                tutor = Cliente(nomeCliente, telefone, email, cpf, endereco, pets)
                clientes.append(tutor)

            atendimento = Atendimento(data=str(data.date()), hora=hora, animal=animal, tutor=tutor, motivo=result_input, tipo=result_input_tipo, pagamento=None, situacao=False)
            controle_agendamento.agendarConsulta(atendimento)
        elif indice_menu == 2:
            print([str(a) for a in controle_agendamento.listarAgendamentos()])
        elif indice_menu == 3:
            cpf = input("Digite o cpf do cliente: ")
            nomeAnimal = input("Digite o nome do animal")
            confirmacao = input("Deseja realmente cancelar o agendamento?(s/n)")
            if confirmacao == "s":
                controle_agendamento.cancelarConsulta(cpf, nomeAnimal)
            else:
                print("O agendamento ainda esta disponivel!")
        elif indice_menu == 4:
            for cliente in clientes:
                cliente.toString()
        elif indice_menu == 5:
            controle_agendamento.adicionarPrescicao()
        elif indice_menu == 6:
            controle_agendamento.obterPrescricoes()
        elif indice_menu == 7:
            break
 
render_agendamentos()

