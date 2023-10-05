from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        try:
            res = self.db.collection.insert_one(motorista)
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista_by_id(self, id):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler o motorista: {e}")
            return None

    def update_motorista(self, id, novos_dados):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": novos_dados})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def delete_motorista(self, id):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None