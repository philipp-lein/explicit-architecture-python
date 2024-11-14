import os
import django
from django.core.management import call_command

from src.ApplicationCore.Component.User.Application.Repository.Django.user_repository import UserRepository
from src.ApplicationCore.Component.User.Service.user_service import UserService

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.Infrastructure.DjangoProject.settings')  # Adjust to match your settings module path
django.setup()
from src.Infrastructure.Persistence.Django.django_persistence_service import DjangoPersistenceService
from src.Infrastructure.Persistence.Django.entity.user import UserEntity

def run_migrations():
    """
    Run migrations to ensure the database schema is up-to-date.
    """
    print("Running migrations...")
    call_command('migrate')
    print("Migrations completed.")

def add_user(username):
    # TODO make this injectable and initialize it elsewhere
    persistence_service = DjangoPersistenceService()
    user_repository = UserRepository(persistence_service)
    user_service = UserService(user_repository)

    user_service.create_user(username)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create a new user.")
    parser.add_argument('username', type=str, help="Username")

    args = parser.parse_args()

    add_user(args.username)
