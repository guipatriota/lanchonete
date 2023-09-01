'''
Classe Produto de integração com o 
Banco de dados na tabela Produto
'''
from lanchonete_db import LanchoneteDB

class Produto:
    '''
    Classe Produto de integração com o 
    Banco de dados na tabela Produto.
    '''
    def __init__(self):
        self.lanchonete_db = LanchoneteDB()

    def inserir(self, nome, quantidade, valor, unidade_medida):
        '''Insere novo produto.'''
        query = '''INSERT INTO Produto
                   (Nome, Quantidade, Valor, UnidadeMedida)
                   VALUES (%s, %s, %s, %s)'''
        return self.lanchonete_db.execute_query(query, (nome,
                                          quantidade,
                                          valor,
                                          unidade_medida))

    def listar(self):
        '''Lista todos os produtos.'''
        query = "SELECT * FROM Produto"
        return self.lanchonete_db.fetch_all_records(query)

    def listar_nome_por_id(self, id_produto):
        '''Lista nome do produto dado seu ID.'''
        query = "SELECT Nome FROM Produto WHERE IdProduto = %s"
        return self.lanchonete_db.fetch_one_record(query, [id_produto])

    def get_last_insert_id(self):
        '''Recupera último ID criado.'''
        query = "SELECT LAST_INSERT_ID()"
        result = self.lanchonete_db.fetch_one_record(query)
        if result:
            return result[0]
        return None
    