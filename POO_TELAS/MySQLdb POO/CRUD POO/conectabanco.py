import MySQLdb  # Importa a biblioteca do MySQL


class ConectaBanco:  # Define a classe
    def __init__(self):  # init é o metodo inicializador da classe
        self.con = ""  # Cria a variavel de conexão vazia

    def conecta(self):  # Método para conectar no banco
        host = "localhost"  # Nome utilizado no host no Workbenck
        user = "PythonProjects"  # Nome do usuario que criamos no Workbenck
        password = "123456"  # Senha que colocamos para o usuario
        db = "bd_escola"  # Nome do banco de dados
        port = 3306  # Porta configurada para o server MySQL
        self.con = MySQLdb.connect(host, user, password, db, port)  # Na variavel con cria nossa conexão

    def select(self, campos, tabelas, where=None):  # Definie o método, o paramêtro where é opcional.
        self.conecta()  # Cria a conexão com o banco
        cur = self.con.cursor()  # Cria uma variavel do tipo cursor que permite executar query SQL.
        query = ("SELECT "+campos+" FROM " + tabelas)  # Cria a query
        if where:  # Caso tenha um parametro where
            query = (query + " WHERE " + where)  # Adiciona where na query
        cur.execute(query)  # Executa um Select através do cur
        result = cur.fetchall()  # fetchall vai gerar uma tupla com os registros encontrados
        self.con.close()  # Encerra a conexão com o banco
        return result  # Retorna o(s) resultado(s) obtido(s)

    def insert(self, tabela, valores, campos=None):  # Definie o método, campos é opcional.
        self.conecta()  # Cria a conexão com o banco
        cur = self.con.cursor()  # Cria uma variavel do tipo cursor que permite executar query SQL.
        query = ("INSERT INTO " + tabela)  # Adiciona a tabela a qual sera inseriso o registro
        if campos:  # Caso haja especificação de campos
            query = (query + "("+campos+")")  # Adiciona os campos na query
        query = (query + " VALUES(" + valores+")")  # Adiciona os valores a query
        print(query)  # Apenas para visualizar a query que esta sendo executada...
        cur.execute(query)  # Executa o Insert através do cur
        self.con.commit()  # Executa o commit
        self.con.close()  # Encerra a conexão com o banco

    def update(self, tabela, sets, where=None):  # Definie o método, o paramêtro where é opcional.
        self.conecta()  # Cria a conexão com o banco
        cur = self.con.cursor()  # Cria uma variavel do tipo cursor que permite executar query SQL.
        query = ("UPDATE " + tabela + " SET " + sets)  # Cria a query
        if where:  # Caso tenha um parametro where
            query = (query + " WHERE " + where)  # Adiciona where na query
        print(query)  # Apenas para visualizar a query que está sendo executada...
        cur.execute(query)  # Executa um Select através do cur
        self.con.commit()  # Executa o commit
        self.con.close()  # Encerra a conexão com o banco

    def delete(self, tabela, where):  # Definie o método
        self.conecta()  # Cria a conexão com o banco
        cur = self.con.cursor()  # Cria uma variavel do tipo cursor que permite executar query SQL.
        query = ("DELETE FROM " + tabela + " WHERE " + where)  # Cria a query
        print(query)  # Apenas para visualizar a query que está sendo executada...
        cur.execute(query)  # Executa um Select através do cur
        self.con.commit()  # Executa o commit
        self.con.close()  # Encerra a conexão com o banco
