"""
Classe LanchoneteDB de integração com o 
Banco de dados lanchonete e todas as suas tabelas
"""
import os
import mysql.connector
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


class LanchoneteDB:
    """
    Classe de conexão com o banco de dados - tabela lanchonete
    """
    def __init__(self):
        self.connection, self.cursor = self.conectar()

    def conectar(self):
        """Inicia conexão com banco de dados"""
        connection = mysql.connector.connect(
                                            host=DB_HOST,
                                            user=DB_USER,
                                            password=DB_PASSWORD,
                                            database=DB_NAME
                                            )
        cursor = connection.cursor()
        return connection, cursor

        
    def close(self):
        """Encerra conexão com banco de dados."""
        self.cursor.close()
        self.connection.close()
