'''
Classe Cliente de integração com o 
Banco de dados na tabela Cliente
'''
from lanchonete_db import LanchoneteDB

class Cliente:
    '''
    Classe Cliente permite o cadastro de um novo cliente e também a visualização
    dos clientes cadastrados.
    Métodos:
    - inserir(nome, endereço): Bool - Insere novo cliente na tabela Cliente.
    - listar(): Tupple - Lista de todos os nomes dos clientes e seus IDs.
    - listaDados(idCliente): Tupple -  Mostra Nome e Endereço de um cliente.
    '''
    def __init__(self):
        self.lanchonete_db = LanchoneteDB()

    def inserir(self, nome, endereco):
        '''Insere novo cliente na tabela Cliente.'''
        query = "INSERT INTO Cliente (Nome, Endereco) VALUES (%s, %s)"
        return self.lanchonete_db.execute_query(query, (nome, endereco))

    def listar(self):
        '''Lista todos os clientes cadastrados e seus IDs

        Returns:
            tupla: tuplas com ((Nome), (idCliente)) para cada cliente cadastrado
        '''
        query = "SELECT Nome, idCliente FROM Cliente"
        return self.lanchonete_db.fetch_all_records(query)

    def listar_dados(self, id_cliente):
        '''Lista todos os dados de um cliente cadastrado

        Returns:
            tupla: tuplas com os dados do cliente
        '''
        query = "SELECT * FROM Cliente WHERE idCliente = %s LIMIT 1"
        return self.lanchonete_db.fetch_all_records(query, id_cliente)
