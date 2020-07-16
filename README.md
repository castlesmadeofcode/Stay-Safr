# Stay Safr Django App Project Setup

1. Clone down the repo and `cd` into it
1. Set up your virtual environment:
   `python -m venv capstoneenv`
1. Activate virtual environment:
   `source ./capstoneenv/bin/activate`
1. Install dependencies:
   `pip install -r requirements.txt` pip install Pillow
1. Create a Superuser:
   `python manage.py createsuperuser`
1. Run migrations:
   `python manage.py makemigrations capstoneapp`
   `python manage.py migrate`
1. Start the Server:
   `python manage.py runserver`

## ERD

https://dbdiagram.io/d/5ed91fa5e81ffb416774d551
