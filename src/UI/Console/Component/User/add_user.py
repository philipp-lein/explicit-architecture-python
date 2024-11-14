import os
import django

from src.ApplicationCore.Component.User.Application.Repository.Django.user_repository import UserRepository
from src.ApplicationCore.Component.User.Service.user_service import UserService

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.Infrastructure.Django.settings')  # Adjust to match your settings module path
django.setup()
from src.Infrastructure.Persistence.Django.django_persistence_service import DjangoPersistenceService

def add_user(username):
    # TODO make this injectable and initialize it elsewhere
    persistence_service = DjangoPersistenceService()
    user_repository = UserRepository(persistence_service)
    user_service = UserService(user_repository)

    user_service.create_user(username)
    print(f"Successfully added user '{username}'")
