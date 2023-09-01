'''
Classe PedidoCardapio de integração com o 
Banco de dados na tabela PedidoCardapio
'''
from lanchonete_db import LanchoneteDB

class PedidoCardapio:
    '''
    Classe PedidoCardapio permite o gerenciamento das relações entre pedidos e 
    itens do cardápio.
    Métodos:
    - adicionar(IdPedido, IdProduto, Quantidade): Bool - Adiciona novo item da 
                                                         tabela PedidoCardápio.
    - apagar(IdPedidoCardapio): Bool - Exclui um item da tabela PedidoCardápio.
    - listar(): Tupla - Lista de todos os registros da tabela PedidoCardapio.
    - alterar(IdPedidoCardapio, IdPedido, IdProduto, Quantidade): Bool - Altera
                            itens da tabela PedidoCardápio.
    - listar_por_pedido(id_pedido): Tupla - Lista itens da tabela PedidoCardápio
                                            com base no id de um pedido.
    '''
    def __init__(self):
        self.lanchonete_db = LanchoneteDB()

    def adicionar(self, id_pedido, id_cardapio, quantidade):
        ''' Adiciona novo item da tabela PedidoCardápio.'''
        query = '''INSERT INTO PedidoCardapio
                   (IdPedido, IdCardapio, Quantidade)
                   VALUES (%s, %s, %s)'''
        return self.lanchonete_db.execute_query(query, (id_pedido, id_cardapio, quantidade))

    def apagar(self, id_pedido_cardapio):
        '''Exclui um item da tabela PedidoCardápio.'''
        query = "DELETE FROM PedidoCardapio WHERE IdPedidoCardapio = %s"
        return self.lanchonete_db.execute_query(query, (id_pedido_cardapio,))

    def listar(self):
        '''Lista de todos os registros da tabela PedidoCardapio.'''
        query = "SELECT * FROM PedidoCardapio"
        return self.lanchonete_db.fetch_all_records(query)

    def alterar(self, id_pedido_cardapio, id_pedido, id_cardapio, quantidade):
        '''Altera itens da tabela PedidoCardápio.'''
        query = '''UPDATE PedidoCardapio
                   SET IdPedido = %s, IdCardapio = %s, Quantidade = %s 
                   WHERE IdPedidoCardapio = %s'''
        return self.lanchonete_db.execute_query(query, (id_pedido,
                                          id_cardapio,
                                          quantidade,
                                          id_pedido_cardapio))

    def listar_por_pedido(self, id_pedido):
        '''Lista itens da tabela PedidoCardápio com base no id de um pedido.'''
        query = "SELECT * FROM PedidoCardapio WHERE IdPedido = %s"
        return self.lanchonete_db.fetch_all_records(query, [id_pedido])
