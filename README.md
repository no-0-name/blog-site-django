# Django Blog Site

This is a blog site built with Django and Postgresql. The site allows users to create, read, update, and delete blog posts. It also supports user registration and authentication, allowing users to create and manage their own posts.

![blog-photo](https://github.com/no-0-name/blog-site-django/blob/main/blog-django-photo.png)
## Features

- User registration and authentication
- Create accounts and comments
- Create, edit, delete articles
- User-friendly and responsive interface
- Easy to navigate and interact with
- Database powered by Postgresql

## Installation

1. Clone the repository

```bash
git clone https://github.com/no-0-name/blog-site-django.git
```

2. Navigate to the project directory

```bash
cd blog-site-django
```

3. Install the project dependencies

```bash
pip install -r requirements.txt
```

4. Set up the database

   - Install Postgresql and create a new database for the project.
   - Open `blog-site-django/settings.py` and update the `DATABASES` configuration with your database details.

5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the development server

```bash
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
