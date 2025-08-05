import os
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/sisu"


# Cria a 'engine' de conexão com o banco de dados.
# echo=True é útil para debug, pois mostra os comandos SQL gerados.
# Isso é uma fabrica de conexão.
engine = create_engine(DATABASE_URL, echo=True)

with engine.connect() as con:
    sql : str = text("SELECT id,first_name,last_name,age,heigth FROM tb_person ORDER BY first_name")
    result = con.execute(sql)
    print(result)
    for data in result:
        # Tipo de dado retornado pelo sqlalchemy na query.
        print(type(data[0]))
        # Imprimindo o dado para debugging.
        print(data)


    print("-=" * 100)

    print(engine.dialect)
    print(engine.pool.status())
    print(con.connection.dbapi_connection)
    print(engine.url.username)



