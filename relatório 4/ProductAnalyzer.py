from database import Database

db = Database(database="mercado", collection="compras")

class ProductAnalyzer:

    def totalvendas(self): #total de vendas por dia
        pipeline = [
            {"$unwind": "$produtos"},  # desestruturando o array de produtos
            {"$group": {
                "_id": {"data": "$data_compra"},  # aqui eu to pegando uma data de compra
                "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"_id.data": 1}},  # aí eu pego todas as vendas e boto em ordem crescente por data
        ]
        result = list(db.collection.aggregate(pipeline))
        return result

    def produtomaisvendido(self): #produto mais vendido em todas as compras
        pipeline = [
            {"$unwind": "$produtos"},  # desestruturando o array de produtos
            {"$group": {
                "_id": "$produtos.nome",  # estou juntando o nome dos produtos e botando em id
                "produtomaisVendido": {"$sum": "$produtos.quantidade"}
            }},
            {"$sort": {"produtomaisVendido": -1}},  # botando em ordem decrescente
            {"$limit": 1}  # aqui eu to botando um limite que é para aparecer apenas um. Como vai ser em ordem descrecente, ele mostra o primeiro
        ]
        result = list(db.collection.aggregate(pipeline))
        return result

    def clientequemaisGastou(self): #cliente que mais gastou em uma única compra
        pipeline = [
            {"$unwind": "$produtos"},  # desestruturando o array de produtos
            {"$group": {
                "_id": "$cliente_id",  # aqui eu to pegando o id do cliente
                "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"total": -1}},  # bota em ordem decrescente
            {"$limit": 1}  # mostra só um, no caso, só o primeiro
        ]
        result = list(db.collection.aggregate(pipeline))
        return result

    def produtosAcimaDeUmaUnidade(self): #produtos que tiveram uma quantidade vendida superior a uma unidade=
        pipeline = [
            {"$unwind": "$produtos"},  # desestruturando produtos
            {"$match": {"produtos.quantidade": {"$gt": 1}}},  # aqui é tipo um if. No caso seria if(produtos.quantidade > 1)
            {"$group": {
                "_id": "$produtos.nome",  # aqui eu pego o nome do produto e boto em id
                "total": {"$sum": "$produtos.quantidade"}
            }},
        ]
        result = list(db.collection.aggregate(pipeline))
        return result
