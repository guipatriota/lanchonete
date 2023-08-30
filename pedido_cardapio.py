"""
Classe PedidoCardapio de integração com o 
Banco de dados na tabela PedidoCardapio
"""
from lanchonete_db import LanchoneteDB

class PedidoCardapio(LanchoneteDB):
    '''
    Classe PedidoCardapio permite o gerenciamento das relações entre pedidos e itens do cardápio.
    Métodos:
    - adicionar(IdPedido, IdProduto, Quantidade): None
    - apagar(IdPedidoCardapio): None
    - listar(): Lista de todos os registros da tabela PedidoCardapio
    - alterar(IdPedidoCardapio, IdPedido, IdProduto, Quantidade): None
    '''

    def adicionar(self, id_pedido, id_produto, quantidade):
        query = "INSERT INTO PedidoCardapio (IdPedido, IdProduto, Quantidade) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (id_pedido, id_produto, quantidade))
        self.connection.commit()

    def apagar(self, id_pedido_cardapio):
        query = "DELETE FROM PedidoCardapio WHERE IdPedidoCardapio = %s"
        self.cursor.execute(query, (id_pedido_cardapio,))
        self.connection.commit()

    def listar(self):
        query = "SELECT * FROM PedidoCardapio"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def alterar(self, id_pedido_cardapio, id_pedido, id_produto, quantidade):
        query = "UPDATE PedidoCardapio SET IdPedido = %s, IdProduto = %s, Quantidade = %s WHERE IdPedidoCardapio = %s"
        self.cursor.execute(query, (id_pedido, id_produto, quantidade, id_pedido_cardapio))
        self.connection.commit()

    def listar_por_pedido(self, id_pedido):
        query = "SELECT * FROM PedidoCardapio WHERE IdPedido = %s"
        self.cursor.execute(query, [id_pedido])
        return self.cursor.fetchall()
