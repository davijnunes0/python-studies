from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError

class FactoryConnection:

    @staticmethod
    def create_connection(db_user : str,db_password : str,db_name : str):
        try:
             DATABASE_URL : str = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"
             engine = create_engine(DATABASE_URL)
             
             with engine.connect() as conn:
                 conn.execute(text("SELECT 1"))

             return engine
         
        except SQLAlchemyError as e:
            print("Connection error:",e)
            return None
        except Exception as e:
            print("Error:",e)
