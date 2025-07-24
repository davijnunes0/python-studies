from src.main.process_handle import start
from src.model.repository.person_repository import PersonRepository

def main() -> None:

    pass
if __name__ == "__main__":
    person_repository: PersonRepository = PersonRepository()
    person_repository.create_database()
    start()
    