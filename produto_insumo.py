"""
Classe ProdutoInsumo de integração com o 
Banco de dados na tabela ProdutoInsumo
"""
from lanchonete_db import LanchoneteDB

class ProdutoInsumo(LanchoneteDB):
    '''
    Classe ProdutoInsumo permite o gerenciamento das relações entre produtos e insumos.
    Métodos:
    - adicionar(IdProduto, IdInsumo, Quantidade): None
    - apagar(IdProdutoInsumo): None
    - listar(): Lista de todos os registros da tabela ProdutoInsumo
    - alterar(IdProdutoInsumo, IdProduto, IdInsumo, Quantidade): None
    - buscar_por_nome(nome_produto): Retorna os registros do produto pelo nome
    '''

    def adicionar(self, id_produto, id_insumo, quantidade):
        query = "INSERT INTO ProdutoInsumo (IdProduto, IdInsumo, Quantidade) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (id_produto, id_insumo, quantidade))
        self.connection.commit()

    def apagar(self, id_produto_insumo):
        query = "DELETE FROM ProdutoInsumo WHERE IdProdutoInsumo = %s"
        self.cursor.execute(query, (id_produto_insumo,))
        self.connection.commit()

    def listar(self):
        query = "SELECT * FROM ProdutoInsumo"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def alterar(self, id_produto_insumo, id_produto, id_insumo, quantidade):
        query = "UPDATE ProdutoInsumo SET IdProduto = %s, IdInsumo = %s, Quantidade = %s WHERE IdProdutoInsumo = %s"
        self.cursor.execute(query, (id_produto, id_insumo, quantidade, id_produto_insumo))
        self.connection.commit()

    def buscar_por_nome(self, nome_produto):
        query = """SELECT *
                   FROM ProdutoInsumo 
                   INNER JOIN Produto ON ProdutoInsumo.IdProduto = Produto.IdProduto 
                   WHERE Produto.Nome = %s"""
        self.cursor.execute(query, (nome_produto,))
        return self.cursor.fetchall()
