# project_management/main.py
import click
from project_management.commands.user import user
from project_management.commands.project import project
from project_management.commands.task import task
#this commands are registered later after being created
@click.group()
def cli():
    """Project Management CLI"""

cli.add_command(user)   
cli.add_command(project)
cli.add_command(task)

if __name__ == '__main__':
    cli()
