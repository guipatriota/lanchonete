'''
Classe Pedido de integração com o 
Banco de dados na tabela Pedido.
'''
from lanchonete_db import LanchoneteDB

class Pedido:
    '''
    Classe Pedido de integração com o 
    Banco de dados na tabela Pedido.
    '''
    def __init__(self):
        self.lanchonete_db = LanchoneteDB()

    def inserir(self, status, data_hora, id_cliente):
        '''Insere dados na tabela Pedido.'''
        query = '''INSERT INTO Pedido
                   (Status, DataHora, IdCliente, ValorTotal)
                   VALUES (%s, %s, %s, 0.0)'''
        return self.lanchonete_db.execute_query(query, (status, data_hora, id_cliente))

    def listar(self):
        '''Lista dados da tabela Pedido.'''
        query = "SELECT * FROM Pedido"
        return self.lanchonete_db.fetch_all_records(query)

    def atualizar_status(self, id_pedido, novo_status):
        '''Atualiza status de pedido na tabela Pedido.'''
        query = "UPDATE Pedido SET Status = %s WHERE IdPedido = %s"
        return self.lanchonete_db.execute_query(query, (novo_status, id_pedido))

    def listar_por_status(self, status):
        '''Lista pedidos pelo status.'''
        query = '''SELECT Pedido.idPedido,
                          Pedido.Status,
                          Pedido.DataHora,
                          Cliente.Nome
                   FROM Pedido
                   INNER JOIN Cliente ON Pedido.IdCliente = Cliente.idCliente
                   WHERE Pedido.Status = %s'''
        return self.lanchonete_db.fetch_all_records(query, [status])

    def get_last_insert_id(self):
        '''Recupera o último ID inserido em alguma tabela do banco lanchonete.'''
        query = "SELECT LAST_INSERT_ID()"
        result = self.lanchonete_db.fetch_one_record(query)
        if result:
            return result[0]
        return None
