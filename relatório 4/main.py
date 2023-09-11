from database import Database
from writeAJson import writeAJson
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

# 1.Média de gasto total:
""" result = db.collection.aggregate([
     {"$unwind": "$produtos"}, #desestruturar o array
     {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}, #pegar o total de produtos, fazendo a multiplicação do preço pela quantidade, depois somando tudo e atribuindo à variável total
     {"$group": {"_id": None, "media": {"$avg": "$total"}}} #faço a média de tudo
])

writeAJson(result, "Média de gasto total") """

# # Cliente que mais comprou em cada dia:
""" result = db.collection.aggregate([
     {"$unwind": "$produtos"},
     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
     {"$sort": {"_id.data": 1, "total": -1}},
     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
])

writeAJson(result, "Cliente que mais comprou em cada dia") """

# # Produto mais vendido:
""" result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])

writeAJson(result, "Produto mais vendido") """

analyzer = ProductAnalyzer()  #aqui to instanciando um objeto 
resultado_total_vendas = analyzer.totalvendas()  #chama o método totalvendas

print()
print("Resultado das vendas:")
for produto in resultado_total_vendas: #for para percorrer o array
     print(produto)

resultado_produtomaisvendido = analyzer.produtomaisvendido() #chama o método produtomaisvendido

print()
print("O produto mais ventido foi: ")
for(produto) in resultado_produtomaisvendido:
     print(produto)

print()

resutado_clientequemaisgastou =  analyzer.clientequemaisGastou() #chama o método clientequemaisgastou
print("Cliente que mais gastou:")
for produto in resutado_clientequemaisgastou:
     print(produto)

print()

resultado_produtosacimadeumaunidade = analyzer.produtosAcimaDeUmaUnidade()

print("Os produtos que foram vendidos acima de uma unidade foram: ")
for produto in resultado_produtosacimadeumaunidade:
     print(produto)