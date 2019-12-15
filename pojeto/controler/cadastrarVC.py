from pojeto.banco.CadastrarVendasM import CadastrarVendasM

class CadastrarVC:
    def __init__(self, produto:str, preco:float, quantidade:int, franquia:str):
        try:
            self.produto:str = produto
            self.preco:float = preco
            self.quantidade:int = quantidade
            self.franquia:str = franquia
        except:
            print("Erro")
    def CadastrarVenda(self):
        cadastrar = CadastrarVendasM(self.produto, self.preco, self.quantidade, self.franquia)
        return cadastrar.cadastroVenda()