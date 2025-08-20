from sqlalchemy import create_engine

DATABASE_URL : str = "postgresql://postgres:12345@localhost:5432/sisu"
# Factory
engine = create_engine(DATABASE_URL,echo=True) 

print(engine)
print("-=" * 100)
print(engine.dialect)

connection = engine.connect()
print(connection.connection.dbapi_connection)

print("-=" * 100)
print(engine.pool.status())

print("-=" * 100)
print(engine.pool)

connection.close()