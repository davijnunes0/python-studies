from sqlalchemy import (    
create_engine,text, 
MetaData,Table,Column,
PrimaryKeyConstraint,Integer,
String,
DateTime,
inspect,
select,
insert,
update,
delete
)
from datetime import datetime

DATABASE_URL : str = "postgresql://postgres:12345@localhost:5432/sisu"
# Factory
engine = create_engine(DATABASE_URL,echo=True) 

# Vendo detalhes de configurações do banco de dados
"""
print(engine)
print("-=" * 100)
print(engine.dialect)

connection = engine.connect()
print(connection.connection.dbapi_connection)

print("-=" * 100)
print(engine.pool.status())

print("-=" * 100)
print(engine.pool)
"""

with engine.connect() as connection:
    sql = text("SELECT first_name, last_name FROM tb_persons ORDER BY first_name")
    result = connection.execute(sql)
    print(result.fetchmany(2))


"""
 Metadados são dados sobre dados é como você ter uma tabela pessoa tendo dados como primeiro nome, sobrenome.
"""
metadata = MetaData()

# Mapeia a tabela para ser criada no banco de dados.
table_comments = Table("comments", metadata,
                       Column("id",Integer(),nullable=False),
                       Column("name",String(),nullable=False),
                       Column("comment",String(),nullable=False),
                       Column("live",String(),nullable=False),
                       Column("created_at",DateTime(), nullable=True),
                       PrimaryKeyConstraint("id")
                       )

# Usamos o motor do SQLALCHEMY para criar a tabela no banco de dados.
metadata.create_all(engine)

inspect = inspect(engine)

# Verifica o nome das tabelas que temos no banco de dados.
print(inspect.get_table_names())
print("-=" * 100)

# Verifica o nome das colunas da tabela "tb_persons"
print(inspect.get_columns("tb_persons"))
print("-=" * 100)

# Verifica o nome das colunas da tabela "tb_comments"
print(inspect.get_columns("comments"))

print("-=" * 100)
print("-=" * 100)

# Pegando a referência no banco de dados da tabela Comments
comments = Table("comments",metadata,autoload_with=engine)
print(comments.c)
print(comments.columns)
print(comments.c.id)

print("-=" * 100)

# O próprio framework já faz uma consulta para o programador de aplicação.
sql = select(comments.c.id, 
             comments.c.name,
             comments.c.comment).where(
                 comments.c.name == "dunossauro"
             )

with engine.connect() as connection:
    # Pega o resultado do select
    result = connection.execute(sql)
    # Imprime todas as rows presente na consulta
    print(result.first())

print("-=" * 200)

tb_persons = Table("tb_persons",metadata,autoload_with=engine)

# Fazendo uma consulta mais complexa utilizando query builder()
"""
stmt_select = select(tb_persons.c.id,
               tb_persons.c.first_name,
               tb_persons.c.last_name,
               tb_persons.c.age).where(
                   # Connectando condições na cláusula where
                   (tb_persons.c.first_name == "Davi") & (tb_persons.c.age < 30)
                   ).order_by (
                   tb_persons.c.first_name
                  )

"""

# Fazendo uma consulta no banco de dados.
stmt = select(tb_persons.c.id,
              tb_persons.c.first_name,
              tb_persons.c.last_name,
              tb_persons.c.age,
).order_by(tb_persons.c.first_name)

# Fazendo uma deleção no banco com where para deletar um elemento específico
"""
stmt_delete = delete(tb_persons).where(
    tb_persons.c.first_name == "Camila",
    tb_persons.c.last_name == "Nunes",
    tb_persons.c.age == 41
)
"""


# Fazendo uma inserção no banco de dados na tabela comments
"""
stmt_insert = insert(comments).values(
    name="dunossauro",
    comment="LLL",
    live="youtube",
    created_at=datetime.now()
)

"""
# Fazendo um update no banco de dados na tabela tb_persons
"""
stmt_update = update(comments).where(
    comments.c.name == "dunossauro",
    comments.c.comment == "LLL",
    comments.c.live == "youtube",
).values(
    comment="Pei"
)
"""

# Fazendo um update no banco de dados na tabela tb_persons
""""
stmt_update = update(tb_persons).where(
    tb_persons.c.id == 2
).values(
    first_name="Camila",
    last_name="Nunes",
    age=41,
    heigth=1.68,
)
"""

# Abre uma conexão utilizando o motor que construimos
with engine.connect() as connection:
    
    # Executa a consulta
    result = connection.execute(stmt)
    # Pegamos o resultado da consulta
    print(result.fetchall())
