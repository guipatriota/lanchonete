"""
Classe Pedido de integração com o 
Banco de dados na tabela Pedido
"""
from lanchonete_db import LanchoneteDB

class Pedido(LanchoneteDB):
    def inserir(self, status, data_hora, id_cliente):
        query = "INSERT INTO Pedido (Status, DataHora, IdCliente, ValorTotal) VALUES (%s, %s, %s, 0.0)"
        self.cursor.execute(query, (status, data_hora, id_cliente))
        self.connection.commit()

    def listar(self):
        query = "SELECT * FROM Pedido"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def atualizar_status(self, id_pedido, novo_status):
        query = "UPDATE Pedido SET Status = %s WHERE IdPedido = %s"
        self.cursor.execute(query, (novo_status, id_pedido))
        self.connection.commit()
    
    def listar_por_status(self, status):
        query = """
            SELECT Pedido.idPedido, Pedido.Status, Pedido.DataHora, Cliente.Nome
            FROM Pedido
            INNER JOIN Cliente ON Pedido.IdCliente = Cliente.idCliente
            WHERE Pedido.Status = %s
            """
        self.cursor.execute(query, [status])
        return self.cursor.fetchall()
    
    def get_last_insert_id(self):
        query = "SELECT LAST_INSERT_ID()"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None