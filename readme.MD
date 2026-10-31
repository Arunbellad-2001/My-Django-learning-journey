# Day 1 – Introduction to Django and Environment Setup

## 1. What is Django?

Django is a **Python web framework** used to build websites and web applications.

It helps developers create websites quickly and easily without writing everything from scratch.

### Why use Django?

- It is built using Python.
- It helps us develop websites faster.
- It provides built-in security features.
- It supports database operations.
- It provides an admin panel.
- It follows the MVT architecture.

## 2. Django Architecture (MVT)

Django follows the **MVT (Model – View – Template)** architecture.

MVT has three main parts:

### 1. Model

- Model handles the database.
- It stores and manages application data.
- It helps us perform database operations.

### 2. View

- View handles the application logic.
- It receives requests from users.
- It gets data from the Model and sends it to the Template.

### 3. Template

- Template handles the user interface.
- It contains HTML files.
- It displays data to the user.

### MVT Architecture Diagram

```text
          User
            |
            v
           URL
            |
            v
           View
          /    \
         v      v
       Model  Template
         |       |
         v       v
      Database  HTML
                  |
                  v
             User Response
```

## 3. How Django Works

1. The user sends a request through the browser.
2. Django checks the URL.
3. The URL sends the request to the correct View.
4. The View handles the application logic.
5. If required, the View gets data from the Model.
6. The View sends data to the Template.
7. The Template creates the HTML response.
8. Django sends the response back to the browser.

## 4. Django Installation and Environment Setup

I used **Windows CMD (Command Prompt)** to install Django and create my first project.

### Step 1: Install Virtualenv Wrapper

```cmd
pip install virtualenvwrapper-win
```

This package helps us create and manage virtual environments easily.

### Step 2: Create a Virtual Environment

```cmd
mkvirtualenv AS
```

Here, `AS` is the name of my virtual environment.

To activate it later:

```cmd
workon AS
```

### Step 3: Install Django

```cmd
pip install django
```

To check the Django version:

```cmd
django-admin --version
```

### Step 4: Create a Project Folder

```cmd
mkdir project
cd project
```

- `mkdir project` – Creates a folder named project.
- `cd project` – Moves into the project folder.

### Step 5: Create a Django Project

```cmd
django-admin startproject my_first_django_project
```

Move into the Django project folder:

```cmd
cd my_first_django_project
```

To see the project files:

```cmd
dir
```

### Django Project Structure

```text
my_first_django_project/
│
├── manage.py
│
└── my_first_django_project/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### Important Files

| File | Purpose |
|---|---|
| `manage.py` | Used to run Django commands |
| `settings.py` | Contains project settings |
| `urls.py` | Manages URL routing |
| `asgi.py` | Used to deploy Django with ASGI servers |
| `wsgi.py` | Used to deploy Django with WSGI servers |
| `__init__.py` | Makes the folder a Python package |

### Step 6: Run the Django Development Server

```cmd
python manage.py runserver
```

After running this command, Django starts the development server.

I got this URL in CMD:

```text
http://127.0.0.1:8000/
```

Open this URL in your browser to see the Django welcome page.

**Note:** `127.0.0.1` is the local computer address, and `8000` is the default Django development server port.

To stop the server:

```text
CTRL + C
```

---

## 5. Important Commands – Quick Revision

| Command | Use |
|---|---|
| `pip install virtualenvwrapper-win` | Install virtual environment manager |
| `mkvirtualenv AS` | Create a virtual environment |
| `workon AS` | Activate the environment |
| `pip install django` | Install Django |
| `django-admin --version` | Check Django version |
| `mkdir project` | Create a folder |
| `cd project` | Move into a folder |
| `django-admin startproject my_first_django_project` | Create a Django project |
| `dir` | Display files and folders |
| `python manage.py runserver` | Start the Django server |

## 6. What I Learned Today

- What Django is and why we use it.
- Django MVT architecture.
- How Django processes a user request.
- How to install Django.
- How to create and activate a virtual environment.
- How to create my first Django project.
- How to run the Django development server.

**Day 1 completed – Successfully created and ran my first Django project!** 🚀

# Day 2 – Creating a Django App and URL Routing

## 1. What is a Django App?

A Django project can contain multiple apps.

An **app** is a small part of a Django project that handles a specific task.

For example:
- `calc` – Calculator application.
- `blog` – Blog application.
- `accounts` – User account application.
- `products` – Product management application.

**Difference between Project and App:**

- Project – The complete website or web application.
- App – A specific part of the project.

## 2. Creating a Django App Using CMD

First, open CMD and move to your Django project directory.

### Step 1: Activate the Virtual Environment

```cmd
workon AS
```

This activates my virtual environment named `AS`.

### Step 2: Create a Django App

Make sure you are inside the folder containing `manage.py`.

Run:

```cmd
python manage.py startapp calc
```

This creates a new Django app named `calc`.

### Step 3: Check the Created Files

```cmd
dir
```

Open the `calc` folder to see the files created by Django.

### Django App Structure

```text
calc/
│
├── migrations/
│   └── __init__.py
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

### Important Files

| File | Purpose |
|---|---|
| `admin.py` | Used to manage data through the admin panel |
| `apps.py` | Contains app configuration |
| `models.py` | Used to create database models |
| `tests.py` | Used to write test cases |
| `views.py` | Handles requests and returns responses |
| `migrations/` | Stores database migration files |

## 3. Creating urls.py Inside the App

Django does not automatically create a `urls.py` file inside a new app.

So, create a new file named `urls.py` inside the `calc` folder.

**calc/urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### Explanation

- `from django.urls import path` – Imports the path function.
- `from . import views` – Imports views from the current app.
- `urlpatterns` – Stores the URL patterns of the app.
- `path('', views.home, name='home')` – Connects the home URL to the home view.

## 4. Creating a View

Open `calc/views.py`.

Write the following code:

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")
```

### Explanation

- `HttpResponse` – Sends a simple response to the browser.
- `home()` – A view function that handles the request.
- `request` – Contains information about the user's request.
- `HttpResponse("Hello World")` – Displays Hello World in the browser.

## 5. Connecting App URLs to Project URLs

Now we need to connect the `calc` app URLs to the main Django project.

Open:

`my_first_django_project/urls.py`

Import `include` from `django.urls`.

**Project urls.py**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('calc.urls')),
    path('admin/', admin.site.urls),
]
```

### Explanation

- `include` – Connects the URL patterns of another app.
- `path('', include('calc.urls'))` – Connects the main website URL to the `calc` app URLs.
- `path('admin/', admin.site.urls)` – Connects the Django admin panel URL.

## 6. Run the Django Server

Go back to CMD.

Run:

```cmd
python manage.py runserver
```

Open this URL in your browser:

```text
http://127.0.0.1:8000/
```

### Expected Output

```text
Hello World
```

Congratulations! My first Django app is working successfully.

---

## 7. How URL Routing Works in Django

When a user opens the website, Django follows this process:

```text
          Browser
              |
              v
       Project urls.py
              |
              v
         calc/urls.py
              |
              v
         views.py
              |
              v
      HttpResponse()
              |
              v
           Browser
```

1. The user opens `http://127.0.0.1:8000/`.
2. Django checks the project `urls.py`.
3. `include()` sends the URL to `calc/urls.py`.
4. The app URL connects to the `home()` function.
5. The view returns `Hello World`.
6. The browser displays the response.

## 8. Important Commands – Quick Revision

| Command | Use |
|---|---|
| `workon AS` | Activate virtual environment |
| `python manage.py startapp calc` | Create a Django app |
| `dir` | Display files and folders |
| `python manage.py runserver` | Start Django server |

## 9. What I Learned Today

- What is a Django app?
- Difference between a Django project and an app.
- How to create an app using CMD.
- How to create `urls.py` inside an app.
- How to create a view using `HttpResponse`.
- How to connect app URLs with project URLs using `include()`.
- How URL routing works in Django.

**Day 2 completed – Successfully created my first Django app and displayed Hello World in the browser!** 🚀