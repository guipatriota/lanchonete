'''
Classe LanchoneteDB de integração com o 
Banco de dados lanchonete e todas as suas tabelas
'''
import os
import mysql.connector
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

class SingletonMeta(type):
    '''
    Classe para definir o padrão de projeto Singleton para a 
    classe LanchoneteDB, que ao ser herdada pelas demais classes, mantém sempre
    apenas 1 instância e garante apenas 1 acesso ao banco de dados.
    '''
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class LanchoneteDB(metaclass=SingletonMeta):
    '''
    Classe de conexão com o banco de dados - tabela lanchonete
    '''
    def __init__(self):
        self.connection, self.cursor = self.conectar()

    def conectar(self):
        '''Inicia conexão com banco de dados'''
        connection = mysql.connector.connect(
                                            host=DB_HOST,
                                            user=DB_USER,
                                            password=DB_PASSWORD,
                                            database=DB_NAME
                                            )
        cursor = connection.cursor()
        return connection, cursor

    def execute_query(self, query, params=None):
        '''Executa uma query SQL e gerencia exceções.'''
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True

        except mysql.connector.Error as error:
            print(f"Erro ao executar a query: {error}")
            self.connection.rollback()  # Desfaz as alterações em caso de erro
            return False
    
    def fetch_all_records(self, query, params=None):
        '''Executa uma query de SELECT e retorna todos os registros.'''
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

        except mysql.connector.Error as error:
            print(f"Erro ao buscar registros: {error}")
            return None

    def fetch_one_record(self, query, params=None):
        '''Executa uma query de SELECT e retorna o primeiro registro.'''
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            
            record = self.cursor.fetchone()
            return record

        except mysql.connector.Error as error:
            print(f"Erro ao buscar registro: {error}")
            return None

    def close(self):
        '''Encerra conexão com banco de dados.'''
        self.cursor.close()
        self.connection.close()
