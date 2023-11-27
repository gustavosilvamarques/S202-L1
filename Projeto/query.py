class QueryDatabase:
    def __init__(self, database):
        self.db = database

    #Relacionamentos
    def create_cadastro_policial(self, nome):
        #Faz o cadastro do medico no hospital
        query = "MATCH (pri:Prisao {nome: $nome}),(p:Policial) CREATE (pri)-[:TEM]->(p)"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def create_cadastro_bandido(self, nome):
        #Faz o cadastro do paciente no hospital
        query = "MATCH (pri:Prisao {nome: $nome}),(b:Bandido) CREATE (pri)-[:TEM]->(b)"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def create_prender(self, nome_policial, nome_bandido):
        #Faz uma consulta do paciente para o medico
        query = "MATCH (p:Policial {nome: $nome_policial}),(b:Bandido {nome: $nome_bandido}) CREATE (p)-[:PRENDE]->(b)"
        parameters = {"nome_policial": nome_policial, "nome_bandido": nome_bandido}
        self.db.execute_query(query, parameters)

    #Gets
    def get_prisao(self):
        query = "MATCH (pri:Prisao) RETURN pri"
        results = self.db.execute_query(query)
        return [result["pri"] for result in results]
    
    def get_policiais(self):
        query = "MATCH (p:Policial) RETURN p"
        results = self.db.execute_query(query)
        return [result["p"] for result in results]
    
    def get_bandidos(self):
        query = "MATCH (b:Bandido) RETURN b"
        results = self.db.execute_query(query)
        return [result["b"] for result in results]
    
    