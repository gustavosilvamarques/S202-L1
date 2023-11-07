class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

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


class TeacherCLI(SimpleCLI):
    def __init__(self, person_model):
        super().__init__()
        self.person_model = person_model
        self.add_command("create", self.create_person)
        self.add_command("read", self.read_person)
        self.add_command("update", self.update_person)
        self.add_command("delete", self.delete_person)

    def create_person(self):
        name = input("Entre com o nome do professor: ")
        ano_nasc = int(input("Entre com o ano de nascimento do professor: "))
        cpf = input("Entre com o cpf: ")
        self.person_model.create_person(name, ano_nasc, cpf)

    def read_person(self):
        name = input("Entre com o professor que desejar ler: ")
        teacher = self.person_model.read_teacher(name)
        if teacher:
            teacher = teacher[0]
            print(f"Nome do professor: {teacher['name']}")
            print(f"Ano de nascimento do professor: {teacher['ano_nasc']}")
            print(f"CPF do professor: {teacher['cpf']}")

    def update_person(self):
        name = input("Entre com a novo nome do professor: ")
        cpf = input("Entre com o novo CPF do professor: ")
        self.person_model.update_teacher(name, cpf)

    def delete_person(self):
        name = input("Entre com o nome do professor que deseja deletar: ")
        self.person_model.delete_person(name)
        
    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        
