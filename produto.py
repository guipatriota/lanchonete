"""
Classe Produto de integração com o 
Banco de dados na tabela Produto
"""
from lanchonete_db import LanchoneteDB

class Produto(LanchoneteDB):
    def inserir(self, nome, quantidade, valor, unidade_medida):
        query = ("INSERT INTO Produto "+
                "(Nome, Quantidade, Valor, UnidadeMedida) "+
                "VALUES (%s, %s, %s, %s)")
        self.cursor.execute(query, (nome, quantidade, valor, unidade_medida))
        self.connection.commit()

    def listar(self):
        query = "SELECT * FROM Produto"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def listar_nome_por_id(self, id_produto):
        query = "SELECT Nome FROM Produto WHERE IdProduto = %s"
        self.cursor.execute(query, (id_produto,))
        return self.cursor.fetchall()

    def get_last_insert_id(self):
        query = "SELECT LAST_INSERT_ID()"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None
    