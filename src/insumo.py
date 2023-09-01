'''
Classe Insumo de integração com o 
Banco de dados na tabela Insumo
'''
from lanchonete_db import LanchoneteDB

class Insumo:
    '''
    Classe Insumo permite o cadastro de um novo insumo e também a visualização
    dos insumos cadastrados.
    Métodos:
    - inserir(nome, categoria, unidade_medida, quantidade, preco): Bool - Insere
                                            novo insumo na tabela Insumo.
    - listar(): Tupple - Lista de todos os insumos e seus IDs
    - buscar_por_nome(self, nome_insumo): IdInsumo|None - Retorna id de insumo.
    - listar_dados(idInsumo): Tupple - Todos os dados de um insumo específico
    '''
    def __init__(self):
        self.lanchonete_db = LanchoneteDB()

    def inserir(self, nome, categoria, unidade_medida, quantidade, preco):
        '''Insere novo insumo na tabela Insumo.'''
        query = '''INSERT INTO Insumo
                   (Nome, Categoria, UnidadeMedida, Quantidade, Preco)
                   VALUES (%s, %s, %s, %s, %s)'''
        return self.lanchonete_db.execute_query(query, (nome,
                                          categoria,
                                          unidade_medida,
                                          quantidade,
                                          preco))

    def listar(self):
        '''Lista todos os insumos cadastrados e seus IDs

        Returns:
            tupla: tuplas com todos os dados de cada insumo cadastrado
        '''
        query = "SELECT * FROM Insumo"
        return self.lanchonete_db.fetch_all_records(query)

    def buscar_por_nome(self, nome_insumo):
        '''Retorna id de insumo.'''
        query = "SELECT IdInsumo FROM Insumo WHERE Nome = %s LIMIT 1"
        result = self.lanchonete_db.fetch_one_record(query, (nome_insumo,))
        if result:
            return result[0]
        return None


    def listar_dados(self, id_insumo):
        '''Lista todos os dados de um insumo específico

        Returns:
            tupla: tuplas com os dados do insumo
        '''
        query = "SELECT * FROM Insumo WHERE idInsumo = %s LIMIT 1"
        return self.lanchonete_db.fetch_all_records(query, (id_insumo,))
