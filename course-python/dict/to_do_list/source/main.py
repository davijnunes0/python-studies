from source.unitTest.test_connection import TestFactoryConnection
from source.model.person import Person


def main():
   
   testConnection = TestFactoryConnection()
   testConnection.test_create_connection_success()


if __name__ == "__main__":
    main()