import pytest
from sqlalchemy.engine.base import Engine
from sqlalchemy.exc import SQLAlchemyError
from source.connection.connection_factory import FactoryConnection

class TestFactoryConnection:

    def test_create_connection_success(self):
        """Testa se a conexão é criada corretamente com parâmetros válidos"""
        # Configuração
        db_user = "test_user"
        db_password = "test_pass"
        db_name = "test_db"
        
        # Execução
        engine = FactoryConnection.create_connection(
            db_user=db_user,
            db_password=db_password,
            db_name=db_name
        )
        
        # Verificação
        assert isinstance(engine, Engine)
        assert engine.url.drivername == "postgresql"
        assert engine.url.username == db_user
        assert engine.url.password == db_password
        assert engine.url.database == db_name

    def test_create_connection_with_invalid_credentials(self):
        """Testa se exceção é lançada com credenciais inválidas"""
        with pytest.raises(SQLAlchemyError):
            FactoryConnection.create_connection(
                db_user="invalid_user",
                db_password="wrong_pass",
                db_name="nonexistent_db"
            )