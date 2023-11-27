from Policial import Policial
from Bandido import Bandido
from Prisao import Prisao

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, nome, function):
        self.commands[nome] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class PrisaoCLI(SimpleCLI):
    def __init__(self, prisao_model):
        super().__init__()
        self.prisao_model = prisao_model
        self.add_command("create_policial", self.create_policial)
        self.add_command("read_policial", self.read_policial)
        self.add_command("update_policial", self.update_policial)
        self.add_command("delete_policial", self.delete_policial)
        self.add_command("create_bandido", self.create_bandido)
        self.add_command("read_bandido", self.read_bandido)
        self.add_command("update_bandido", self.update_bandido)
        self.add_command("delete_bandido", self.delete_bandido)
        self.add_command("create_prision", self.create_prision)
        self.add_command("read_prision", self.read_prision)
        self.add_command("update_prision", self.update_prision)
        self.add_command("delete_prision", self.delete_prision)

    def create_prision(self):
        nome = input("Entre com o nome da prisão: ")
        local = input ("Entre com o local da prisão: ")
        Prision = Prisao(nome, local) 
        self.prisao_model.create_prisao(Prision)
        print("***Prisão criada com sucesso!***")

    def read_prision(self):
        nome = input("Entre com o nome da prisão que deseja ler: ")
        prision = self.prisao_model.read_prision(nome)

        if prision:
            prision = prision[0]
            print(f"Nome da prisão: {prision['nome']}")
            print(f"Local da prisão: {prision['local']}")

    def update_prision(self):
        nome = input("Entre com o nome da prisão que deseja atualizar: ")
        local = ("Entre com a novo local da prisão: ")
        self.prisao_model.update_policial(nome, local)
        print("***Policial atualizado com sucesso!***")
        

    def delete_prision(self):
        nome = input("Entre com o nome da prisão que deseja excluir: ")
        self.prisao_model.delete_prision(nome)
        print("***Prisão deletada com sucesso!***")


    #CLI Policial
    def create_policial(self):
        nome = input("Entre com o nome do policial: ")
        idade = int(input("Entre com a idade do policial: "))
        numeroDistintivo = int(input("Entre com o número do distintivo do policial: "))
        departamento = input("Entre com o departamento do policial: ")
        Policiais = Policial(nome, idade, numeroDistintivo, departamento)
        if idade >= 18 and idade <= 70 and numeroDistintivo >= 0:
            self.prisao_model.create_policial(Policiais)
            print("***Policial criado com sucesso***")
        else:
            print("Algum valor invalido, criar novamente outro policial")

    def read_policial(self):
        nome = input("Entre com o nome do policial que deseja ler: ")
        policial = self.prisao_model.read_policial(nome)
        if policial:
            policial = policial[0]
            print(f"Nome do policial: {policial['nome']}")
            print(f"Idade do policial: {policial['idade']}")
            print(f"Número do distintivo do policial: {policial['numeroDistintivo']}")
            print(f"Departamento do policial: {policial['departamento']}")

    def update_policial(self):
        nome = input("Entre com o nome do policial que deseja atualizar: ")
        idade = int(input("Entre com a nova idade do policial: "))
        numeroDistintivo = int(input("Entre com o novo número do distintivo do policial: "))
        departamento = input("Entre com o novo departamento do policial: ")
        if idade >= 18 and idade <= 40 and numeroDistintivo >= 0:
            self.prisao_model.update_policial(nome, idade, numeroDistintivo, departamento)
            print("***Policial atualizado com sucesso***")
        else:
            print("Algum valor invalido, atualize o policial novamente")

    def delete_policial(self):
        nome = input("Digite o nome do policial que deseja excluir: ")
        self.prisao_model.delete_policial(nome)
        print("***Policial deletado com sucesso***")

    #CLI Bandido
    def create_bandido(self):
        nome = input("Entre com o nome do bandido: ")
        idade = int(input("Entre com a idade do bandido: "))
        cpf = input("Entre com o cpf do bandido: ")
        fichaCriminal = input("Entre com a ficha criminal do bandido: ")
        Bandidos = Bandido(nome, idade, cpf, fichaCriminal)
        if idade > 0 and idade <= 150:
            self.prisao_model.create_bandido(Bandidos)
            print("***Bandido criado com sucesso***")
        else:
            print("Algum valor invalido, crie outro bandido")

    def read_bandido(self):
        nome = input("Entre com o nome do bandido que deseja ler: ")
        bandido = self.prisao_model.read_bandido(nome)
        if bandido:
            bandido = bandido[0]
            print(f"Nome do bandido: {bandido['nome']}")
            print(f"Idade do bandido: {bandido['idade']}")
            print(f"CPF do bandido: {bandido['cpf']}")
            print(f"Ficha criminal do bandido: {bandido['fichaCriminal']}")

    def update_bandido(self):
        nome = input("Entre com o nome do bandido que deseja atualizar: ")
        idade = int(input("Entre com a nova idade do bandido: "))
        cpf = input("Entre com o novo cpf do bandido: ")
        fichaCriminal = input("Entre com a nova ficha criminal do bandido: ")
        if idade > 0 and idade <= 150:
            self.prisao_model.update_bandido(nome, idade, cpf, fichaCriminal)
            print("***Bandido atualizado com sucesso***")
        else:
            print("Algum valor invalido, atualize novamente os dados do bandido")

    def delete_bandido(self):
        nome = input("Digite o nome do bandido que deseja excluir: ")
        self.prisao_model.delete_bandido(nome)
        print("***Bandido deletado com sucesso***")
    
    def run(self):
        print("Welcome to the Prision, CLI!")
        print("Available commands: create_prision, read_prision, update_prision, delete_prision, create_policial, read_policial, update_policial,"
        + " delete_policial, create_bandido, read_bandido, update_bandido, delete_bandido, create_relacionamentos, quit")
        super().run()