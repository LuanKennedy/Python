from pojeto.banco.CadastrarProdutoM import CadastrarProdutoM


class CadastrarPC:
    def __init__(self, produto:str, validade, preco:float, quantidade:int):
        try:
            self.produto:str = produto
            self.validade = validade
            self.preco:float = preco
            self.quantidade:int = quantidade
            self.existe = True
        except:
            print("felipe")
    def existeP(self):
        existe = CadastrarProdutoM(self.produto, self.validade, self.preco, self.quantidade)
        existeB = existe.existeProduto()
        if existeB:
            return True
            print("Produto já Cadastrado")
        else:
            return False

    def cadastrarP(self):
        existe = self.existeP()
        if existe:
            return False
        else:
            cadastrar = CadastrarProdutoM(self.produto, self.validade, self.preco, self.quantidade)
            cadastrar.cadastroProduto()
            return True

    def atualizaP(self):
        update = CadastrarProdutoM(self.produto, self.validade, self.preco, self.quantidade)
        return update.updateProduto()

    def selectP(self):
        meupal= CadastrarProdutoM(self.produto, self.validade, self.preco, self.quantidade)
        return meupal.selectModal()

    def deleteP(self):
        delete = CadastrarProdutoM(self.produto, self.validade, self.preco, self.quantidade)
        return delete.deleteProduto()

