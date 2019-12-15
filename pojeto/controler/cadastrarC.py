from pojeto.banco.cadastrarM import Cadastro

class Cadastrar:


    def __init__(self,usuario,senha,email):
        self.usuario = usuario
        self.senha = senha
        self.email = email


    def existeC(self):
        existe = Cadastro(self.usuario,self.senha,self.email)
        existeB = existe.existeEmail()
        if existeB:
            return False
            print("Usuario já Cadastrado")
        else:
            return True


    def cadastrarC(self):
        existe = self.existeC()
        if existe:
            cadastrar = Cadastro(self.usuario,self.senha,self.email)
            cadastrar.cadastroPessoa()
            return True
        else:
            return False



