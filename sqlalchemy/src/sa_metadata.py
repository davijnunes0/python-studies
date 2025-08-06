import sqlalchemy as sa
from sqlalchemy import create_engine,MetaData,select

# Schemas / Types

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/sisu"

# Cria a 'engine' de conexão com o banco de dados.
# echo=True é útil para debug, pois mostra os comandos SQL gerados.
# Isso é uma fabrica de conexão.

engine = create_engine(DATABASE_URL, echo=True)
metadata = sa.MetaData()

# Irá criar a tabela tb_comments no banco de dados sisu, usando metadados.

table = sa.Table("tb_comments",
                 metadata,
                 sa.Column("id",sa.Integer,nullable=False),
                 sa.Column("name",sa.String,nullable=False),
                 sa.Column("comment",sa.String(),nullable=False),
                 sa.Column("live",sa.String(),nullable=False),
                 sa.Column("created_at",sa.DateTime(),nullable=True),
                 sa.PrimaryKeyConstraint("id"),
)
metadata.create_all(engine)


inspect = sa.inspect(engine)
# Pega todos os nomes na tabela do banco de dados
print(inspect.get_table_names())
# Pega o nome de todas as colunas tb_comments
print(inspect.get_columns("tb_comments"))
# Pega o nome de todas as colunas tb_comments
table_comments = sa.Table("tb_comments",metadata,autoload_with=engine)

print("-=" * 1000)

sql = select(table_comments)
print(sql)

with engine.connect() as con:
    result = con.execute(sql)
    print(result.fetchmany(10))