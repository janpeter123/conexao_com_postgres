import psycopg2
from psycopg2 import sql

#Autor: Jan Peter Merkel
#Build Labs - IBM
#Escopo do script: Manipulação básica de um banco de dados Postgres com Python e Psycopg2

# Definindo o objeto de credenciais do banco de dados
pg_credentials = {
    "dbname": "postgres", #deixar padrão
    "user": "<USERNAME>",
    "password": "<PASSWORD>",
    "host": "xxxxxxxxxxx.databases.appdomain.cloud",
    "port": 32377,
    "sslmode": "verify-full",
    "sslrootcert": "./cert.pem" #verifique se o arquivo cert possui a extensão .pem explicita, igual no diretório atual
}

pg_connection = None

#definindo o formato de datas caso necessário
dt_fmt = "%d/%m/%Y"


#Use sempre o try para testar a conexão
#caso a conexão seja recusada, o erro aparecerá no Except.
#Ficará mais legível para quem executa o script

try:
    # Conectando ao Postgres
    pg_connection = psycopg2.connect(**pg_credentials)
    print("Conexao feita com sucesso")
    
    #cria um cursor do postgres
    pg_cursor = pg_connection.cursor()

    #Criando o nome de uma tabela
    name_Table = "teste2"
    
    # Configurando o statement para criar uma tabela
    sqlCreateTable = "create table "+name_Table+" (id bigint, title varchar(128), summary varchar(256), story text);"

    # Executando o comando de criar a tabela
    # alternativa: pg_cursor.execute("CREATE TABLE ... ")

    pg_cursor.execute(sqlCreateTable)
    print(f"Criando a tabela {name_Table}")

    # Obtendo a lista de tabelas existentes
    print("Listando tabelas existentes...")
    pg_cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    print(pg_cursor.fetchall())

    print("Fazendo commit no banco de dados")
    pg_connection.commit()
    

except (Exception, psycopg2.Error) as exception_msg:
    print("Exception: {}".format(exception_msg))
