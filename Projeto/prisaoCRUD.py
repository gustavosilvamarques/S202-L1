from Bandido import Bandido
from Policial import Policial
from Prisao import Prisao

class PrisaoCRUDDB:
    def __init__(self, database):
        self.db = database

    #Criar prisão
    def create_prisao(self, prisao:Prisao):
        query = "CREATE (:Prisao {nome: $nome, local: $local})"
        parameters = {"nome": prisao.nome, "local": prisao.local}
        self.db.execute_query(query, parameters)

    #CRUD Policial
    def create_policial(self, Policiais:Policial):
        query = "CREATE (:Policial {nome: $nome, idade: $idade, numeroDistintivo: $numeroDistintivo, departamento: $departamento})"
        parameters = {"nome": Policiais.nome, "idade": Policiais.idade, "numeroDistintivo": Policiais.numeroDistintivo, "departamento": Policiais.departamento}
        self.db.execute_query(query, parameters)
    
    def read_policial(self, nome):
        query = "MATCH (p:Policial {nome: $nome}) RETURN p"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["p"] for result in results]
    
    def update_policial(self, nome, nova_idade, novo_numeroDistintivo, novo_departamento):
        query = "MATCH (p:Policial {nome: $nome}) SET p.idade = $nova_idade, p.numeroDistintivo = $novo_numeroDistintivo, p.departamento = $novo_departamento"
        parameters = {"nome": nome, "nova_idade": nova_idade, "novo_numeroDistintivo": novo_numeroDistintivo, "novo_departamento": novo_departamento}
        self.db.execute_query(query, parameters)

    def delete_policial(self, nome):
        query = "MATCH (p:Policial {nome: $nome}) DETACH DELETE p"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    #CRUD bandido
    def create_bandido(self, Bandidos:Bandido):
        query = "CREATE (:Bandido {nome: $nome, idade: $idade, cpf: $cpf, fichaCriminal: $fichaCriminal})"
        parameters = {"nome": Bandidos.nome, "idade": Bandidos.idade, "cpf": Bandidos.cpf, "fichaCriminal": Bandidos.fichaCriminal}
        self.db.execute_query(query, parameters)
    
    def read_bandido(self, nome):
        query = "MATCH (b:Bandido {nome: $nome}) RETURN b"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["b"] for result in results]

    def update_bandido(self, nome, nova_idade, novo_cpf, nova_fichaCriminal):
        query = "MATCH (b:Bandido {nome: $nome}) SET b.idade = $nova_idade, b.cpf = $novo_cpf, b.fichaCriminal = $nova_fichaCriminal"
        parameters = {"nome": nome, "nova_idade": nova_idade, "novo_cpf": novo_cpf, "nova_fichaCriminal": nova_fichaCriminal}
        self.db.execute_query(query, parameters)


    def delete_bandido(self, nome):
        query = "MATCH (b:Bandido {nome: $nome}) DETACH DELETE b"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)





    

    

    


    

    