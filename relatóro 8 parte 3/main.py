from database import Database
from match import Game # Importe a classe GameDatabase, substituindo 'match' por 'game' se necessário

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.238.222.103:7687", "neo4j", "transportation-boresights-beliefs")
db.drop_all()

# Criando uma instância da classe GameDatabase para interagir com o banco de dados
game_db = Game(db)  # Substitua a instância da classe para GameDatabase

# Criando alguns jogadores
game_db.create_player("Alice")
game_db.create_player("Bob")
game_db.create_player("Charlie")

# Criando algumas partidas e registrando os jogadores que participaram
game_db.create_match("Match1")
game_db.add_player_to_match("Alice", "Match1")
game_db.add_player_to_match("Bob", "Match1")

game_db.create_match("Match2")
game_db.add_player_to_match("Alice", "Match2")
game_db.add_player_to_match("Charlie", "Match2")

# Atualizando o nome de um jogador
game_db.update_player("Alice", "Alicia")

# Deletando um jogador e uma partida
game_db.delete_player("Charlie")
game_db.delete_match("Match2")

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(game_db.get_players())
print("Partidas:")
print(game_db.get_matches())
print("Partidas de Alicia:")
print(game_db.get_player_matches("Alicia"))

# Fechando a conexão com o banco de dados
db.close()
