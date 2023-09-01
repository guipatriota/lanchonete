'''
Classe CardapioProduto de integração com o 
Banco de dados na tabela CardapioProduto
'''
from lanchonete_db import LanchoneteDB

class CardapioProduto:
    '''
    Classe CardapioProduto permite o gerenciamento das relações entre cardápios 
    e produtos.
    Métodos:
    - adicionar(IdCardapio, IdProduto, Quantidade): Bool - Adiciona novo item.
    - apagar(IdCardapioProduto): Bool - Exclui item.
    - listar(): Tupple - Lista de todos os registros da tabela CardapioProduto
    - alterar(IdCardapioProduto,
              IdCardapio, 
              IdProduto, 
              Quantidade): Bool - Altera itens na tabela CardapioProduto.
    - listar_por_cardapio(IdCardapio): Tupple - Mostra os dados do item 
                                                IdCardapio
    '''
    def __init__(self):
        self.lanchonete_db = LanchoneteDB()

    def adicionar(self, id_cardapio, id_produto, quantidade):
        '''Adiciona novo item.'''
        query = '''INSERT INTO CardapioProduto 
                   (IdCardapio, IdProduto, Quantidade) 
                   VALUES (%s, %s, %s)'''
        return self.lanchonete_db.execute_query(query, (id_cardapio, id_produto, quantidade))

    def apagar(self, id_cardapio_produto):
        '''Exclui item.'''
        query = "DELETE FROM CardapioProduto WHERE IdCardapioProduto = %s"
        return self.lanchonete_db.execute_query(query, (id_cardapio_produto,))

    def listar(self):
        '''Lista de todos os registros da tabela CardapioProduto'''
        query = "SELECT * FROM CardapioProduto"
        return self.lanchonete_db.fetch_all_records(query)

    def alterar(self, id_cardapio_produto, id_cardapio, id_produto, quantidade):
        '''Altera itens na tabela CardapioProduto'''
        query = '''UPDATE CardapioProduto
                   SET IdCardapio = %s, IdProduto = %s, Quantidade = %s
                   WHERE IdCardapioProduto = %s'''
        return self.lanchonete_db.execute_query(query, (id_cardapio,
                                          id_produto,
                                          quantidade,
                                          id_cardapio_produto))

    def listar_por_cardapio(self, id_cardapio):
        '''Mostra os dados do item IdCardapio'''
        query = "SELECT * FROM CardapioProduto WHERE IdCardapio = %s"
        return self.lanchonete_db.fetch_all_records(query, [id_cardapio])
