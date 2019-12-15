from pojeto.banco.conexao import Conexao


class Login:
    login = ""
    senha = ""
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha


    def autenticar(self):
        autenticacao = Conexao()
        resultado = autenticacao.select("login_usuario,senha_usuario","tbl_usuario",(f'login_usuario = "{self.login}" and senha_usuario = "{self.senha}" '))
        return len(resultado) > 0


