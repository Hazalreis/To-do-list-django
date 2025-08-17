# Django To-Do List Project

A simple Django-based To-Do application for task management with user authentication.

## Overview
This is a simple **Django** project for a To-Do List application.  
Users can register, log in, add tasks, update them, and delete them.  
The project focuses on core functionalities with user-specific task protection.

## Features
- User registration, login, and logout.
- View all tasks belonging to the logged-in user.
- Create new tasks.
- Update existing tasks.
- Delete tasks.
- Access control: only logged-in users can manage their tasks.

## Technologies Used
- Python 3
- Django
- HTML & CSS (simple design)
- SQLite (default database)

## Project Structure
- `models.py`: Task model definition and user relationship.
- `forms.py`: TaskForm and RegisterForm.
- `views.py`: All views (list, create, update, delete tasks, and user registration).
- `urls.py`: URL routing for all pages.
- `templates/todolist/`: HTML templates for each page.



# Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows


# Install dependencies:

pip install -r requirements.txt


# Apply migrations:

python manage.py migrate


# Run the development server:

python manage.py runserver



# Open your browser and go to:

http://127.0.0.1:8000/



# Notes
Each task is linked to the user who created it.
