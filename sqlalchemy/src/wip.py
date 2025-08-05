import os
from sqlalchemy import create_engine,text,select,Table,MetaData,insert,update,delete
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/sisu"


# Cria a 'engine' de conexão com o banco de dados.
# echo=True é útil para debug, pois mostra os comandos SQL gerados.
# Isso é uma fabrica de conexão.
engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()

# Pegando os metadados da tabela tb_person.
table_person = Table("tb_person",metadata,autoload_with=engine)
# Definition Query Language (DQL)
query_to_table_person  = select(table_person.c.id,
                              table_person.c.first_name,
                              table_person.c.last_name,
                              table_person.c.heigth)


# Forma de inserir um usuário no banco de dados 
sql_to_table_person_insert =  insert(table_person).values(first_name="Artur",last_name="Bahia",age=20,heigth=1.70)

# Forma de atualizar um usuário no banco de dados
stmt_to_table_person_update = update(table_person).where(table_person.c.id == 1).values(
    first_name="Davi",last_name="José Nunes",age=20,heigth=1.91
)

# Forma de excluir um usuário no banco de dados
stmt_to_table_person_delete = delete(table_person).where(table_person.c.id == 1)

with engine.connect() as con:

    """
    # sql : str = text("SELECT id,first_name,last_name,age,heigth FROM tb_person ORDER BY first_name")
    # result = con.execute(sql)
    # print(result)
    # for data in result:
        # print(type(data))
        # Tipo de dado retornado pelo sqlalchemy na query.
        #print(type(data[0]))
        # Imprimindo o dado para debugging.
        #print(data)
    """

    # result_insert = con.execute(sql_to_table_person_insert)
    # print(result_insert)

    # result_update = con.execute(stmt_to_table_person_update)
    # print(result_update)

    # result_delete = con.execute(stmt_to_table_person_delete)
    # print(result_delete)

    result = con.execute(query_to_table_person)
    print(result.fetchmany(4))

    print("-=" * 100)

    print(engine.dialect)
    print(engine.pool.status())
    print(con.connection.dbapi_connection)
    print(engine.url.username)



