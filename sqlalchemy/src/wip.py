import os
from sqlalchemy import create_engine,text,select,Table,MetaData
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
sql_to_table_person  = select(table_person.c.id,
                              table_person.c.first_name,
                              table_person.c.heigth
                              ).where(table_person.c.age > 20)

print(sql_to_table_person)

with engine.connect() as con:
    # sql : str = text("SELECT id,first_name,last_name,age,heigth FROM tb_person ORDER BY first_name")
    # result = con.execute(sql)
    # print(result)
    # for data in result:
        # print(type(data))
        # Tipo de dado retornado pelo sqlalchemy na query.
        #print(type(data[0]))
        # Imprimindo o dado para debugging.
        #print(data)

    result = con.execute(sql_to_table_person)
    print(result.fetchmany(3))

    print("-=" * 100)

    print(engine.dialect)
    print(engine.pool.status())
    print(con.connection.dbapi_connection)
    print(engine.url.username)



