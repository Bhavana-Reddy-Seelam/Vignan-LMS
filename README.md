# Vignan LMS

A Django-based learning management system (LMS) built with modular apps for users, courses, quizzes, assignments, forums, and certificates.

## Project Overview

This project includes the following Django apps:
- `users` – custom user model and auth support
- `courses` – course creation, enrollment, lessons, progress, and analytics
- `quizzes` – quizzes, questions, and result tracking
- `assignments` – assignment submission management
- `forums` – discussion forums and comments
- `certificates` – certificate generation and tracking

The project uses Django admin UI customization via `django-jazzmin`.

## Requirements

- Python 3.14
- Django 6.0.5
- django-jazzmin 3.0.4
- Pillow 12.2.0
- sqlparse 0.5.5
- tzdata 2026.2

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Bhavana-Reddy-Seelam/Vignan-LMS.git
   cd lms_project
   ```

2. Create and activate a virtual environment:

   Windows PowerShell:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   Windows CMD:
   ```cmd
   python -m venv .venv
   .\.venv\Scripts\activate.bat
   ```

   macOS / Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open the app in your browser:

   ```text
   http://127.0.0.1:8000/
   ```

## Notes

- The project is configured for SQLite by default via `db.sqlite3`.
- `DEBUG` is enabled in `lms_project/settings.py`; do not use this configuration in production.
- The `.gitignore` file excludes the virtual environment, SQLite database file, and common Python artifacts.
- A simple root homepage route at `/` has been added, so `http://127.0.0.1:8000/` now shows a welcome page and `/admin/` opens the Django admin interface.

## Project Validation

The Django project has been validated successfully with:
- `python manage.py check`

## Contributing

Feel free to open issues or submit pull requests for bug fixes, feature improvements, or documentation updates.
