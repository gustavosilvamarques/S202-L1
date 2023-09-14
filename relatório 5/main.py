from database import Database
from writeAJson import writeAJson
from BookCRUD import BookCRUD
from BookCLI import BookCLI

db = Database(database="relatorio_05", collection="livros")
BookCRUD = BookCRUD(database=db) #conectando o crud no database

bookCLI = BookCLI(BookCRUD) #é a CLI que eu vou rodar(no caso, é uma função da classe BookCLI)
bookCLI.run()
