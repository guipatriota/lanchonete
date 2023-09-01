'''
Classe ProdutoInsumo de integração com o 
Banco de dados na tabela ProdutoInsumo
'''
from lanchonete_db import LanchoneteDB

class ProdutoInsumo:
    '''
    Classe ProdutoInsumo permite o gerenciamento das relações entre produtos e 
    insumos.
    Métodos:
    - adicionar(IdProduto, IdInsumo, Quantidade): Bool - Adiciona novo item na 
                                                         tabela ProdutoInsumo.
    - apagar(IdProdutoInsumo): Bool - Apaga item.
    - listar(): Tupla - Lista de todos os registros da tabela ProdutoInsumo
    - alterar(IdProdutoInsumo, IdProduto, IdInsumo, Quantidade): Bool - Altera
                                                        Item da tabela.
    - buscar_por_nome(nome_produto): Tupla - Retorna os registros do produto 
                                             pelo nome.
    '''
    def __init__(self):
        self.lanchonete_db = LanchoneteDB()

    def adicionar(self, id_produto, id_insumo, quantidade):
        '''Adiciona novo item na tabela ProdutoInsumo.'''
        query = '''INSERT INTO ProdutoInsumo
                   (IdProduto, IdInsumo, Quantidade) VALUES (%s, %s, %s)'''
        return self.lanchonete_db.execute_query(query, (id_produto, id_insumo, quantidade))

    def apagar(self, id_produto_insumo):
        '''Apaga item da tabela ProdutoInsumo.'''
        query = "DELETE FROM ProdutoInsumo WHERE IdProdutoInsumo = %s"
        return self.lanchonete_db.execute_query(query, (id_produto_insumo,))

    def listar(self):
        '''Lista todos os itens da tabela ProdutoInsumo.'''
        query = "SELECT * FROM ProdutoInsumo"
        return self.lanchonete_db.fetch_all_records(query)

    def alterar(self, id_produto_insumo, id_produto, id_insumo, quantidade):
        '''Altera item da tabela ProdutoInsumo.'''
        query = '''UPDATE ProdutoInsumo
                   SET IdProduto = %s, IdInsumo = %s, Quantidade = %s 
                   WHERE IdProdutoInsumo = %s'''
        return self.lanchonete_db.execute_query(query, (id_produto,
                                          id_insumo,
                                          quantidade,
                                          id_produto_insumo))

    def buscar_por_nome(self, nome_produto):
        '''Busca item na tabela ProdutoInsumo pelo nome de um produto.'''
        query = '''SELECT *
                   FROM ProdutoInsumo 
                   INNER JOIN Produto ON ProdutoInsumo.IdProduto = Produto.IdProduto 
                   WHERE Produto.Nome = %s'''
        return self.lanchonete_db.fetch_all_records(query, (nome_produto,))
