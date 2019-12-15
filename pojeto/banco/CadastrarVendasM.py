from pojeto.banco.conexao import Conexao
from pojeto.banco.CadastrarProdutoM import CadastrarProdutoM

class CadastrarVendasM:
    def __init__(self, produto, preco, quantidade, franquia):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade
        self.franquia = franquia


    def cadastroVenda(self):
        insert = Conexao()
        insert.insert('tbl_vendas', f"'{self.produto}','{self.preco}', '{self.quantidade}','{self.franquia}'",
                      'nome_venda, preco_venda , quantidade_venda, franquia')
        return insert
