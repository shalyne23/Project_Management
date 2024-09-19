# project_management/commands/user.py
import click
from project_management.database import User, session

@click.group()
def user():
    """User management commands"""

@user.command()
@click.option('--name', prompt='User Name', help='Name of the user')
def create(name):
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f'User {name} created.')

@user.command()
def list():
    users = session.query(User).all()
    user_data = [{"ID": user.id, "Name": user.name} for user in users]
    print(user_data)

@user.command()
@click.argument('user_id', type=int)
@click.option('--new_name', prompt='New Name', help='New name for the user')
def update(user_id, new_name):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.name = new_name
        session.commit()
        print(f'User {user_id} updated.')
    else:
        print(f'User with ID {user_id} does not exist.')

@user.command()
@click.argument('user_id', type=int)
def delete(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f'User {user.name} (ID: {user.id}) deleted.')
    else:
        print(f'User with ID {user_id} does not exist.')
