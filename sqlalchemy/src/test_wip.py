
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/sisu"

# Cria a 'engine' de conexão com o banco de dados.
# echo=True é útil para debug, pois mostra os comandos SQL gerados.
# Isso é uma fabrica de conexão.

engine = create_engine(DATABASE_URL, echo=True)
con = engine.connect()


def test_connection_username():
    USERNAME : str = "postgres"
    assert USERNAME == engine.url.username


def test_connection_password():
    PASSWORD : str = "12345"
    assert PASSWORD == engine.url.password

def test_connection_database():
    NAME_DATABASE: str = "sisu"
    assert NAME_DATABASE == engine.url.database