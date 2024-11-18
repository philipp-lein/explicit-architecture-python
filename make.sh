#!/bin/bash

# Check if a command is provided
if [ -z "$1" ]; then
  echo "Usage: ./make.sh <command> [--username=<username>]"
  echo "Available commands:"
  echo "  add_user --username=<username>       Add a new user"
  echo "  init                                Install uv when needed and run initial migrations to create database"
  echo "  make_migrations                     Generate new migrations"
  exit 1
fi

COMMAND=$1
shift # Shift the command argument to process the rest

case $COMMAND in
  add_user)
    # Parse the --username argument
    for arg in "$@"; do
      case $arg in
        --username=*)
          USERNAME="${arg#*=}"
          ;;
        *)
          echo "Invalid argument: $arg"
          exit 1
          ;;
      esac
    done

    if [ -z "$USERNAME" ]; then
      echo "Usage: ./make.sh add_user --username=<username>"
      exit 1
    fi

    # Call the Python function
    uv run python -c "from src.UI.Console.Component.User.add_user import add_user; add_user('$USERNAME')"
    ;;
  init)
    # Install uv if not already installed
    if ! command -v uv &> /dev/null; then
      echo "uv is not installed. Installing uv..."
      curl -LsSf https://astral.sh/uv/0.5.2/install.sh | sh
      if [ $? -ne 0 ]; then
        echo "Failed to install uv. Please check your environment and try again."
        exit 1
      fi
      echo "uv installed successfully."
    else
      echo "uv is already installed."
    fi

    # Run migrations to initialize the database
    echo "Running initial migrations..."
    uv run python manage.py migrate
    if [ $? -eq 0 ]; then
      echo "Database initialized successfully."
    else
      echo "Failed to run migrations. Please check the error above."
      exit 1
    fi
    ;;
  make_migrations)
    # Create new migrations after adding an entity
    echo "Making migrations..."
    uv run python manage.py makemigrations
    if [ $? -eq 0 ]; then
      echo "Migrations generated successfully."
    else
      echo "Failed to generate migrations. Please check the error above."
      exit 1
    fi
    ;;
  *)
    echo "Unknown command: $COMMAND"
    exit 1
    ;;
esac
