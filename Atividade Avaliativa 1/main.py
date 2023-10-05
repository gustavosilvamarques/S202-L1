from database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI
from Motorista import Motorista
from Passageiro import Passageiro
from Corrida import Corrida

db = Database(database="atividade_01", collection="motoristas")
motorista_dao = MotoristaDAO(database = db)
motorista_cli = MotoristaCLI(MotoristaDAO)
motorista_cli.run()

def criar_passageiro(db):
    
    passageiro = Passageiro(nome="João", documento="123456789")
    return passageiro

def criar_corrida(passageiro):
    
    corrida1 = Corrida(nota=5, distancia=10, valor=25.0, passageiro=passageiro)
    return corrida1

def criar_e_inserir_motorista(db):

    passageiro = criar_passageiro(db)

    corrida1 = criar_corrida(passageiro)

  
    motorista = Motorista(corridas=[corrida1])

   
    motorista_id = db.collection.insert_one(motorista.__dict__).inserted_id
    print(f"Motorista criado com id: {motorista_id}")


    criar_e_inserir_motorista(db)


