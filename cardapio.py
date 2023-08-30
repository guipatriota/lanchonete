"""
Classe Cardapio de integração com o 
Banco de dados na tabela Cardapio
"""
from lanchonete_db import LanchoneteDB


class Cardapio(LanchoneteDB):
    """
    Classe Cardapio permite o gerenciamento das informações na tabela cardápio.
    Métodos:
    - inserir(nome,
              descrticao,
              categoria,
              valor,
              disponibilidade): None - Insere dados na tabela cardápio
    - listar(): None - Lista de todos os registros da tabela Cardapio
    - get_nome_por_id(IdCardapio): Nome - Encontra o nome de um item pelo id.
    - get_id_por_nome(Nome): IdCardapio - Encontra o id pelo nome do item
    """
    def inserir(self, nome, descricao, categoria, valor, disponibilidade):
        """Insere dados na tabela cardápio"""
        query = '''INSERT INTO Cardapio
                 (Nome, Descricao, Categoria, Valor, Disponibilidade)
                 VALUES (%s, %s, %s, %s, %s)'''
        self.cursor.execute(query, (nome,
                                    descricao,
                                    categoria,
                                    valor,
                                    disponibilidade))
        self.connection.commit()

    def listar(self):
        """Lista de todos os registros da tabela Cardapio"""
        query = "SELECT * FROM Cardapio"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_nome_por_id(self, id_cardapio):
        """Encontra o nome de um item pelo id."""
        query = "SELECT Nome FROM Cardapio WHERE IdCardapio = %s"
        self.cursor.execute(query,(id_cardapio,))
        return self.cursor.fetchall()

    def get_id_por_nome(self, nome):
        """Encontra o id pelo nome do item"""
        query = "SELECT IdCardapio FROM Cardapio WHERE Nome = %s"
        self.cursor.execute(query,(nome,))
        return self.cursor.fetchall()
