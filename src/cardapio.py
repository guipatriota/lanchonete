'''
Classe Cardapio de integração com o 
Banco de dados na tabela Cardapio
'''
from lanchonete_db import LanchoneteDB


class Cardapio:
    '''
    Classe Cardapio permite o gerenciamento das informações na tabela cardápio.
    Métodos:
    - inserir(nome,
              descrticao,
              categoria,
              valor,
              disponibilidade): Bool - Insere dados na tabela cardápio
    - listar(): Tupla - Lista de todos os registros da tabela Cardapio
    - get_nome_por_id(IdCardapio): Nome - Encontra o nome de um item pelo id.
    - get_id_por_nome(Nome): IdCardapio - Encontra o id pelo nome do item
    '''
    def __init__(self):
        self.lanchonete_db = LanchoneteDB()

    def inserir(self, *args):
        '''Insere dados na tabela cardápio'''
        nome, descricao, categoria, valor, disponibilidade = args
        query = '''INSERT INTO Cardapio
                 (Nome, Descricao, Categoria, Valor, Disponibilidade)
                 VALUES (%s, %s, %s, %s, %s)'''
        return self.lanchonete_db.execute_query(query, (nome,
                                                        descricao,
                                                        categoria,
                                                        valor,
                                                        disponibilidade))

    def listar(self):
        '''Lista de todos os registros da tabela Cardapio'''
        query = "SELECT * FROM Cardapio"
        return self.lanchonete_db.fetch_all_records(query)

    def get_nome_por_id(self, id_cardapio):
        '''Encontra o nome de um item pelo id.'''
        query = "SELECT Nome FROM Cardapio WHERE IdCardapio = %s"
        return self.lanchonete_db.fetch_all_records(query,(id_cardapio,))

    def get_id_por_nome(self, nome):
        '''Encontra o id pelo nome do item'''
        query = "SELECT IdCardapio FROM Cardapio WHERE Nome = %s"
        return self.lanchonete_db.fetch_all_records(query,(nome,))
