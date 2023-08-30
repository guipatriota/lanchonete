"""
Classe CardapioProduto de integração com o 
Banco de dados na tabela CardapioProduto
"""
from lanchonete_db import LanchoneteDB

class CardapioProduto(LanchoneteDB):
    """
    Classe CardapioProduto permite o gerenciamento das relações entre cardápios 
    e produtos.
    Métodos:
    - adicionar(IdCardapio, IdProduto, Quantidade): None - Adiciona novo item.
    - apagar(IdCardapioProduto): None - Exclui item.
    - listar(): Tupple - Lista de todos os registros da tabela CardapioProduto
    - alterar(IdCardapioProduto,
              IdCardapio, 
              IdProduto, 
              Quantidade): None - Altera itens na tabela CardapioProduto.
    - listar_por_cardapio(IdCardapio): Tupple - Mostra os dados do item 
                                                IdCardapio
    """

    def adicionar(self, id_cardapio, id_produto, quantidade):
        """Adiciona novo item."""
        query = '''INSERT INTO CardapioProduto 
                   (IdCardapio, IdProduto, Quantidade) 
                   VALUES (%s, %s, %s)'''
        self.cursor.execute(query, (id_cardapio, id_produto, quantidade))
        self.connection.commit()

    def apagar(self, id_cardapio_produto):
        """Exclui item."""
        query = "DELETE FROM CardapioProduto WHERE IdCardapioProduto = %s"
        self.cursor.execute(query, (id_cardapio_produto,))
        self.connection.commit()

    def listar(self):
        """Lista de todos os registros da tabela CardapioProduto"""
        query = "SELECT * FROM CardapioProduto"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def alterar(self, id_cardapio_produto, id_cardapio, id_produto, quantidade):
        """Altera itens na tabela CardapioProduto"""
        query = '''UPDATE CardapioProduto
                   SET IdCardapio = %s, IdProduto = %s, Quantidade = %s
                   WHERE IdCardapioProduto = %s'''
        self.cursor.execute(query, (id_cardapio,
                                    id_produto,
                                    quantidade,
                                    id_cardapio_produto))
        self.connection.commit()

    def listar_por_cardapio(self, id_cardapio):
        """Mostra os dados do item IdCardapio"""
        query = "SELECT * FROM CardapioProduto WHERE IdCardapio = %s"
        self.cursor.execute(query, [id_cardapio])
        return self.cursor.fetchall()
