# Django Todo Project

This is a simple **Django-based Todo application** with user registration. Users can register, add tasks, view tasks, and delete tasks. 
This project demonstrates the use of Django models, forms, views, and templates.

---

## Features

- User registration
- Add tasks
- View all tasks for a user
- Delete tasks
- Basic template rendering
- Example testing view

---

## Prerequisites

- Python 3.8+
- pip (Python package installer)
- virtualenv (optional but recommended)

---

## Setup Instructions

1. **Clone the repository**
bash

git clone https://github.com/Carshell/Django_To-do-app

cd study

3. Create a virtual environment
# Windows
python -m venv venv
venv\Scripts\activate.bat

# Unix/MacOS
python3 -m venv venv
source venv/bin/activate

3.Install dependencies
  pip install -r requirements.txt

4. Run database migrations
   python manage.py migrate
   
5. Start the development server
  python manage.py runserver

6. Open the application
   Go to your browser and navigate to: http://127.0.0.1:8000/register

Notes
This project uses SQLite as the default database (db.sqlite3), which is suitable for development.
Media and static files are not included and should be set up if deploying.
