from pojeto.banco.conexao import Conexao

class Cadastro:

    def __init__(self,usuario,senha,email):
        self.usuario = usuario
        self.email = email
        self.senha = senha


    def existeEmail(self):
        select = Conexao()
        resultado = select.select(('email_usuario'), ('tbl_usuario'), (f"email_usuario = '{self.email}'"))
        return len(resultado) > 0

    def cadastroPessoa(self):
        existe = self.existeEmail()
        if existe:
            return True
        else:
            insert = Conexao()
            insert.insert('tbl_usuario',f"'{self.usuario}','{self.senha}','{self.email}'", 'login_usuario, senha_usuario, email_usuario')





