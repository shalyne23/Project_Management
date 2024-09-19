# project_management/commands/task.py
import click
from project_management.database import Project, Task, session

@click.group()
def task():
    """Task management commands"""

@task.command()
@click.option('--name', prompt='Task Name', help='Name of the task')
@click.option('--project_id', type=int, prompt='Project ID', help='Project ID for the task')
def create(name, project_id):
    project = session.query(Project).filter_by(id=project_id).first()
    if project:
        task = Task(name=name, project_id=project_id)
        session.add(task)
        session.commit()
        print(f'Task {name} created for project {project.name}.')

@task.command()
def list():
    tasks = session.query(Task).all()
    task_data = [{"ID": task.id, "Name": task.name, "Project": task.project.name} for task in tasks]
    print(task_data)

@task.command()
@click.argument('task_id', type=int)
@click.option('--new_name', prompt='New Name', help='New name for the task')
def update(task_id, new_name):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.name = new_name
        session.commit()
        print(f'Task {task_id} updated.')
    else:
        print(f'Task with ID {task_id} does not exist.')

@task.command()
@click.argument('task_id', type=int)
def delete(task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f'Task {task.name} (ID: {task.id}) deleted.')
    else:
        print(f'Task with ID {task_id} does not exist.')
