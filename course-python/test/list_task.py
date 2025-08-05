from dataclasses import dataclass
from .task import Task

@dataclass
class ListTask:
    def __init__(self):
        self.tasks : list[Tast] = []
        self.count_of_id : int = 1

    def create_task(self,name,status="Pending") -> Task:
        # Task = DOC (Dependency of component)
        new_task = Task(self.count_of_id,name,status)
        self.tasks.append(new_task)
        self.count_of_id += 1
        return new_task

    def update_task(self,identificador: int,name : str | None = None, status: str | None = None) -> None:
        for task in self.tasks:
            if task.id == identificador:
                if name:
                    task.name = name
                if status:
                    task.status = status
                break

    def delete_task(self,identificador : int) -> None:
        for task in self.tasks:
            if task.id == identificador:
                self.tasks.remove(task)
            break


    def recover_task(self,identificador: int) -> Task | None:
        for task in self.tasks:
            if task.id == identificador:
                return task

        return None
