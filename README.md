
<br/>
<div align="center">

<h3 align="center">Daily Planner</h3>
<p align="center">
Amazing way to structure your daily taks


  


</p>
</div>

## About The Project

Daily Planner is a lightweight web application designed to help users efficiently manage their day-to-day tasks. Built using the Django web framework, the app offers a clean and minimal interface that allows users to add, view, edit, mark as complete, and delete tasks with ease. It’s ideal for anyone looking for a simple tool to stay organized without the clutter of unnecessary features.

This project demonstrates the use of Django’s built-in functionalities to implement full CRUD (Create, Read, Update, Delete) operations, along with proper URL routing, templates, and model integration. It serves as a foundational project for beginners looking to explore web development with Django.
### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

- [Django](https://docs.djangoproject.com/en/5.2/)
- [Sqlite](https://docs.djangoproject.com/en/5.2/ref/databases/)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Django Admin](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)
### Installation

1. Clone the repo
   ```sh
    git clone https://github.com/VishhhalGupta/Daily_Planner.git
    cd Daily_Planner
   ```
2. Install NPM packages
   ```sh
   python -m venv env 
   source env/bin/activate 
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations
   ```sh
   python manage.py migrate
   ```
5. Run the development server
   ```sh
   python manage.py runserver
   ```
6. Open in browser
   ```sh
   http://127.0.0.1:8000/
   ```
## Usage

   ```sh
   Daily_Planner/
├── planner/            # Core app
│   ├── models.py       # Task model
│   ├── views.py        # Task views (CRUD logic)
│   ├── templates/      # HTML templates
│   └── urls.py         # App routing
├── Daily_Planner/      # Project config
├── db.sqlite3          # Local database
├── manage.py           # Django management
└── requirements.txt    # Dependencies
   ```
## Acknowledgments

Future Improvements:

  ->User authentication and login-based task views
  ->Task categories or priority levels
  ->Due dates and reminders
  ->Dark mode UI
