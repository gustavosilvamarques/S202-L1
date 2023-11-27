from database import Database
from Prisao import Prisao
from Policial import Policial
from Bandido import Bandido
from prisaoCRUD import PrisaoCRUDDB
from query import QueryDatabase
from cli import PrisaoCLI

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.205.30.74:7687", "neo4j", "subfunctions-echelons-kits")
db.drop_all()

# Criando uma instância da classe prisão para interagir com o banco de dados
prisaoCRUD_db = PrisaoCRUDDB(db)
# Criando uma instância da classe Query para interagir com o banco de dados
query_db = QueryDatabase(db)

#Criando uma prisão
print("\n")
prisao = Prisao("Penitenciária Federal de Alcatraz", "California")
prisaoCRUD_db.create_prisao(prisao)

#CRUD policiais
policial = Policial("Jhon", 53, 6, "Polícia civil")
prisaoCRUD_db.create_policial(policial)
print("Policial:")
print(prisaoCRUD_db.read_policial("Jhon"))
prisaoCRUD_db.update_policial("Jhon", 55, 10, "Segurança e Vigilancia")
#prisaoCRUD_db.delete_policial("Jhon")
print("\n")

#CRUD bandidos
bandido = Bandido("José", 32, "028.313.251-98", "furto")
prisaoCRUD_db.create_bandido(bandido)
print("Bandido: ")
print(prisaoCRUD_db.read_bandido("José"))
prisaoCRUD_db.update_bandido("José", 28, "028.313.251-98", "homicídio" )
#prisaoCRUD_db.delete_bandido("José")
print("\n")

#Relacionamentos
query_db.create_cadastro_policial("Penitenciária Federal de Alcatraz")
query_db.create_cadastro_bandido("Penitenciária Federal de Alcatraz")
query_db.create_prender("Jhon", "José")

# Imprimindo todas as informações do banco de dados
print("Prisão: ")
print(query_db.get_prisao())
print("\n")
print("Policiais: ")
print(query_db.get_policiais())
print("\n")
print("Bandidos")
print(query_db.get_bandidos())
print("\n")

#CLI
PrisaoModel = PrisaoCRUDDB(database=db)
prisaoCLI = PrisaoCLI(PrisaoModel)
prisaoCLI.run()

# Fechando a conexão com o banco de dados
db.close()