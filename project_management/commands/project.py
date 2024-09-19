# project_management/commands/project.py
import click
from project_management.database import User, Project, session

@click.group()
def project():
    """Project management commands"""

@project.command()
@click.option('--name', prompt='Project Name', help='Name of the project')
@click.option('--user_id', type=int, prompt='User ID', help='User ID for the project owner')
def create(name, user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        project = Project(name=name, user_id=user_id)
        session.add(project)
        session.commit()
        print(f'Project {name} created for user {user.name}.')

@project.command()
def list():
    projects = session.query(Project).all()
    project_data = [{
        "ID": project.id,
        "Name": project.name,
        "Owner": project.user.name if project.user else "No owner"
    } for project in projects]
    print(project_data)


@project.command()
@click.argument('project_id', type=int)
@click.option('--new_name', prompt='New Name', help='New name for the project')
def update(project_id, new_name):
    project = session.query(Project).filter_by(id=project_id).first()
    if project:
        project.name = new_name
        session.commit()
        print(f'Project {project_id} updated.')
    else:
        print(f'Project with ID {project_id} does not exist.')

@project.command()
@click.argument('project_id', type=int)
def delete(project_id):
    project = session.query(Project).filter_by(id=project_id).first()
    if project:
        session.delete(project)
        session.commit()
        print(f'Project {project.name} (ID: {project.id}) deleted.')
    else:
        print(f'Project with ID {project_id} does not exist.')
