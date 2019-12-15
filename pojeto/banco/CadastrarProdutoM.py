from pojeto.banco.conexao import Conexao

class CadastrarProdutoM:
    def __init__(self, produto, validade, preco, quantidade):
        self.produto = produto
        self.validade = validade
        self.preco = preco
        self.quantidade = quantidade

    def existeProduto(self):
        select = Conexao()
        resultado = select.select(('nome_produtos'), ('tbl_produtos'), (f"nome_produtos = '{self.produto}'"))
        retornoTrueorFalse = len(resultado) > 0
        return retornoTrueorFalse

    def cadastroProduto(self):
        existe = self.existeProduto()
        if existe:
            return True
        else:
            insert = Conexao()
            insert.insert('tbl_produtos',f"'{self.produto}','{self.validade}','{self.preco}', '{self.quantidade}'", 'nome_produtos, data_validade, preco_produto, quantidade  ')



    def updateProduto(self):
        update = Conexao()
        update.select('quantidade','tbl_produtos',f"nome_produtos = '{self.produto}'")
        return update.update('tbl_produtos',f"quantidade = {self.quantidade}",f"nome_produtos = '{self.produto}'")



    def selectModal(self):
        selectM = Conexao()
        selectP = selectM.select('nome_produtos, data_validade, preco_produto, quantidade','tbl_produtos', f"nome_produtos = '{self.produto}'")
        print(selectP)
        return selectP


    def deleteProduto(self):
        deleteProduto = Conexao()
        delet = deleteProduto.delete('tbl_produtos', f"nome_produtos  = '{self.produto}'")
        return delet