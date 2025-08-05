from asyncio import run
from sqlalchemy import create_engine,text
from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = "postgresql+asyncpg://postgres:12345@localhost:5432/sisu"

engine = create_async_engine(DATABASE_URL)

async def main():
    async with engine.connect() as connection:
       sql : str = text("SELECT id,first_name,last_name,age,heigth FROM tb_person ORDER BY first_name")
       result = await connection.execute(sql)
       
       for data in result:
           print(data)

run(main())