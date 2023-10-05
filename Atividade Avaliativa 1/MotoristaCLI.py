class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, identifier, function):
        self.commands[identifier] = function

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

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista):
        super().__init__()
        self.motorista = motorista
        self.commands = {} 
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)


    def create_motorista(self):
        nome = input("Digite o nome do motorista: ")
        motorista = {"nome": nome}
        motorista_id = self.motorista.create_motorista(motorista)
        if motorista_id:
            print(f"Motorista criado com id: {motorista_id}")

    def read_motorista(self):
        id = input("Digite o id do motorista: ")
        motorista = self.motorista.read_motorista_by_id(id)
        if motorista:
            print(f"Nome: {motorista['nome']}")

    def update_motorista(self):
        id = input("Digite o id do motorista: ")
        nome = input("Digite o novo nome: ")
        novos_dados = {"nome": nome}
        res = self.motorista.update_motorista(id, novos_dados)
        if res:
            print(f"{res} documento(s) modificado(s)")

    def delete_motorista(self):
        id = input("Digite o id do motorista: ")
        res = self.motorista.delete_motorista(id)
        if res:
            print(f"{res} documento(s) deletado(s)")

    def add_command(self, identifier, function):
        self.commands[identifier] = function

    def run(self):
        while True:
            print("\nOpções:")
            print("1. Criar Motorista")
            print("2. Ler Motorista")
            print("3. Atualizar Motorista")
            print("4. Deletar Motorista")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.create_motorista()
            elif opcao == "2":
                self.read_motorista()
            elif opcao == "3":
                self.update_motorista()
            elif opcao == "4":
                self.delete_motorista()
            elif opcao == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
