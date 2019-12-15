# Arquivo principal do programa.
from conectabanco import ConectaBanco  # Importa a classe

banco = ConectaBanco()  # instancia um objeto do tipo ConectaBanco

tabela = "aluno"  # Define a tabela que sera adicionado o registro
'''campos = "idaluno, nome, dtnasc, endereco, cidade, estado, email"  # Define os campos (Opicional)
# Define os valores do novo registro:
valores = "default,'Mauricio Vianna', '1998-09-30', 'Rua D nº 333', 'Cotia','SP', 'mvianna007@gmail.com'"
banco.insert(tabela, valores, campos)  # Executa o método insert, passando os parâmetros

updateset = "nome = 'Vitória Mendes'"
updatewhere = "idaluno = 2"
banco.update(tabela, updateset, updatewhere)  # Executa o método update, passando os parâmetros'''

banco.delete(tabela, "idaluno = 4")  # Executa o método delete, passando os parâmetros

regSelect = banco.select("*", "aluno")  # Executa o método select atribuindo
# o resultado na variavel regSelect
for registro in regSelect:  # Para cada registro na tupla de registros.
    print(registro)  # Imprime o registro.
