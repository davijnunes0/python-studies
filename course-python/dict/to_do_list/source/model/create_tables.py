# create_tables.py
from source.model.create_tables import Base
from source.connection.connection_factory import FactoryConnection

def create_database_tables():
    engine = FactoryConnection.create_connection("postgres", "12345", "db_sales")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_database_tables()