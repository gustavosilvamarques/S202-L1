from database import Database
from teacher_crud import TeacherCRUD
from query import QueryDB
from cli import TeacherCLI

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.91.161.154:7687", "neo4j", "factory-conversion-straws")
query_db = QueryDB(db)

#exercício 1
print("Questão 1 - a -> Busque pelo professor “Teacher” cujo nome seja “Renzo”, retorne o ano_nasc e o CPF: ", query_db.get_renzo())
print("Questão 1 - b -> Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf: ", query_db.get_m())
print("Questão 1 - c -> Busque pelos nomes de todas as cidades “City” e retorne-os: ", query_db.get_city())
print("Questão 1 - d -> Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola\n" 
      "o endereço e o número: ", query_db.get_school())

#exercício 2
print("Questão 2 - a -> Encontre o ano de nascimento do professor mais jovem e do professor mais velho: ", query_db.get_older_and_newer())
print("Questão 2 - b -> Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade 'population': ", query_db.get_average_population())
print("Questão 2 - c -> Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A”: ", query_db.get_city_cep())
print("Questão 2 - d -> Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome: ", query_db.get_third_character())

teacher_crud = TeacherCRUD(db)

# Questão 03 - b(a era só pra criar o CRUD)
teacher_crud.create_teacher('Chris Lima', 1956, '189.052.396-66')

print("Questão 3 - c -> Utilizando a classe TeacherCRUD() pesquise o professor com o name de 'Chris Lima'\n")
print(teacher_crud.read_teacher("Chris Lima"))

print("Utilizando a classe TeacherCRUD() altere o cpf do “Teacher” de name 'Chris Lima' para '162.052.777-77'\n")
teacher_crud.update_teacher('Chris Lima', '162.052.777-77')

TeacherModel = TeacherCRUD(database = db)
teacherCLI = TeacherCLI(TeacherModel)
teacherCLI.run() 

# Fechando a conexão com o banco de dados
db.close()

