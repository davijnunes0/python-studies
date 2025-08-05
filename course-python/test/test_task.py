from .task import Task
from .list_task import ListTask

def test_task_deve_conter_os_campos_id_name__status():

    # Arrange
    identificador : int = 1
    name  : str = "Fazer programa em python"
    status : str = "Pending"

    # Act
    task : Task = Task(identificador,name,status)
    assert task.id == identificador
    assert task.name == name
    assert task.status == status


def test_list_task_create_task():
    # arrange
    ldt = ListTask()
    name : str = "test"
    task : Task = ldt.create_task(name)

    # Assert 
    assert ldt.recover_task(task.id)
    assert task.name == name
    assert task.status =="Pending"

def test_list_task_recover_task():
    ldt = ListTask()

    # Garente que veio None
    assert not ldt.recover_task(10)
