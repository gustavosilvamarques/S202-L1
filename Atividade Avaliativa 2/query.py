class QueryDB:

    def __init__(self, database):
        self.db = database

    #Questão 1 - a
    def get_renzo(self):
        
        query = "MATCH (t:Teacher{name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.ano_nasc"], result["t.cpf"]) for result in results]
    #Questão 1 - b
    def get_m(self):

        query = "MATCH (t:Teacher) where t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.name"], result["t.cpf"]) for result in results]
    
    #Questão 1 - c
    def get_city(self):

        query = "MATCH (c:City) return c.name"
        results = self.db.execute_query(query)
        return [result["c.name"] for result in results]
    
    #Questã 1 - d
    def get_school(self):

        query = "MATCH (s:School) WHERE s.number >= 150 OR s.number <= 550 RETURN s.name, s.address"
        results = self.db.execute_query(query)
        return [(result["s.name"], result["s.address"]) for result in results]
    
    def get_older_and_newer(self):

        query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc), MAX(t.ano_nasc)"
        results = self.db.execute_query(query)
        return [(result["MIN(t.ano_nasc)"], result["MAX(t.ano_nasc)"]) for result in results]
    
    def get_average_population(self):

        query = "MATCH (c:City) WITH AVG(c.population) as avaragePopulation RETURN avaragePopulation"
        results = self.db.execute_query(query)
        return [result["avaragePopulation"] for result in results]
    
    def get_city_cep(self):

        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') as modifiedName"
        results = self.db.execute_query(query)
        return [result["modifiedName"] for result in results]
    
    def get_third_character(self):

        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) as thirdCharacter"
        results = self.db.execute_query(query)
        return [result["thirdCharacter"] for result in results]
    
