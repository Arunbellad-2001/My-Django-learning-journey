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

# Day 3 – Django Template Language (DTL) and HTML Templates

## 1. What is Django Template Language (DTL)?

DTL stands for **Django Template Language**.

It is used to display dynamic data and add simple logic inside HTML files.

Using DTL, we can:
- Display Python variables in HTML.
- Use conditions (`if` and `else`).
- Use loops (`for`).
- Reuse HTML layouts using template inheritance.

**Example:**

```html
<h1>Hello {{ name }}!</h1>
```

Here, `{{ name }}` displays the value of the variable passed from Python.

## 2. Connecting HTML Templates to Django

### Step 1: Configure the Templates Folder

1. Open `settings.py`.
2. Find the `TEMPLATES` section.
3. Add the Templates folder path inside `DIRS`.

First, import `os` at the top of `settings.py`:

```python
import os
```

Update the `DIRS` setting:

```python
'DIRS': [os.path.join(BASE_DIR, 'Templates')],
```

**Note:** The folder name in the setting must match the actual folder name.

### Step 2: Create an HTML File

Create a folder named `Templates` in the main project directory (the folder containing `manage.py`).

Inside the folder, create:

```text
Templates/
    home.html
```

### Step 3: Render the HTML File Using views.py

Open `calc/views.py`.

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

**Explanation:**

- `render()` connects the HTML file to the Django view.
- `'home.html'` is the HTML file we want to display.
- `request` contains information about the user's request.

## 3. Displaying Dynamic Content in HTML

Dynamic content means displaying values from Python inside an HTML page.

### Step 1: Pass Data from views.py

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'Arun'})
```

Here:

- `name` is the variable name.
- `'Arun'` is the value passed from Python.
- The dictionary `{}` is called the context data.

### Step 2: Display the Value in home.html

```html
<h1>Hello {{ name }}!!!</h1>
```

### Expected Output

```text
Hello Arun!!!
```

If we change the value in `views.py`:

```python
return render(request, 'home.html', {'name': 'Rahul'})
```

The browser displays:

```text
Hello Rahul!!!
```

We don't need to change the HTML file every time.

## 4. Changing Background Colour Using HTML

We can change the background colour of a webpage using the HTML `bgcolor` attribute.

For example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Django Project</title>
</head>
<body bgcolor="cyan">

    <h1>Hello Arun!</h1>

</body>
</html>
```

This displays the webpage with a cyan background.

## 5. Django Template Inheritance

Django Template Inheritance allows us to create one common HTML file and reuse its layout in other HTML files.

For example:
- `base.html` – Parent template.
- `home.html` – Child template.
- `about.html` – Another child template.

### Step 1: Create base.html

Create a file named `base.html` inside the Templates folder.

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Django Project</title>
</head>

<body bgcolor="cyan">

    {% block content %}
    {% endblock %}

</body>
</html>
```

**Explanation:**

- `{% block content %}` defines a section that child templates can replace.
- `{% endblock %}` closes the block.

### Step 2: Create home.html

Open `home.html` and write:

```html
{% extends 'base.html' %}

{% block content %}

<h1>Hello {{ name }}!!!</h1>
<p>Welcome to my Django project.</p>

{% endblock %}
```

**Explanation:**

- `{% extends 'base.html' %}` – Inherits the parent template.
- `{% block content %}` – Defines the section where child-page content appears.
- `{% endblock %}` – Ends the block.

### Step 3: Run the Django Server

```cmd
python manage.py runserver
```

Open the browser:

```text
http://127.0.0.1:8000/
```

### Expected Output

You will see:
- Cyan background.
- Hello Arun!!!
- Welcome to my Django project.

## 6. How Template Inheritance Works

```text
           base.html
        (Parent Template)
               |
               |
        {% block content %}
               |
               v
           home.html
        (Child Template)
               |
               v
       Final HTML Page
        Displayed in Browser
```

The parent template provides the common layout, and the child template adds its own content.

## 7. Important DTL Syntax – Quick Revision

| Syntax | Purpose |
|---|---|
| `{{ variable }}` | Displays a variable value |
| `{% extends %}` | Inherits another template |
| `{% block %}` | Defines a replaceable section |
| `{% endblock %}` | Ends a block |
| `{% if %}` | Checks a condition |
| `{% else %}` | Runs when the condition is false |
| `{% for %}` | Repeats content using a loop |

**Remember:** Django template tags are case-sensitive. Always write `block`, not `Block`.

## 8. Important Concepts to Remember

| Concept | Meaning |
|---|---|
| DTL | Django Template Language |
| `render()` | Connects a view with an HTML template |
| Context | Data passed from Python to HTML |
| `{{ }}` | Displays dynamic values |
| `base.html` | Common parent HTML template |
| Template Inheritance | Reuses a common HTML layout |

## 9. What I Learned Today

- What is Django Template Language (DTL)?
- How to connect HTML templates to Django.
- How to configure the Templates folder in `settings.py`.
- How to render HTML files using `render()`.
- How to pass dynamic content from Python to HTML.
- How to change the webpage background colour.
- How to use Django Template Inheritance.
- How to reuse a common HTML layout across multiple pages.

**Day 3 completed – Successfully connected HTML templates to Django, displayed dynamic content, and learned Template Inheritance!** 🚀

# Day 4 – Adding Two Numbers Using Django

## 1. What I Learned Today

Today, I learned how to:
- Create an HTML form in Django.
- Get input from users.
- Send form data to Django views.
- Use the GET method to receive form data.
- Access form values using `request.GET`.
- Convert string values into integers using `int()`.
- Perform addition using Python.
- Display the result on another HTML page.

## 2. Creating an HTML Form

First, open `home.html` and create a form to get two numbers from the user.

**home.html**

```html
{% extends 'base.html' %}

{% block content %}

<h1>Addition of Two Numbers</h1>

<form action="add">
    Enter First Number:
    <input type="text" name="num1"><br><br>

    Enter Second Number:
    <input type="text" name="num2"><br><br>

    <input type="submit" value="Add">

</form>

{% endblock %}
```

### Explanation

- `<form>` – Creates an HTML form.
- `action="add"` – Sends the form data to the `add` URL.
- `<input>` – Creates an input field.
- `name="num1"` – Gives a name to the first input field.
- `name="num2"` – Gives a name to the second input field.
- `type="submit"` – Creates a button to submit the form.

## 3. Creating a Result HTML Page

Create another HTML file named `result.html` inside the Templates folder.

**result.html**

```html
{% extends 'base.html' %}

{% block content %}

<h1>Addition Result</h1>

Result: {{ result }}

{% endblock %}
```

### Explanation

- `extends` – Inherits the common layout from `base.html`.
- `block content` – Defines the section for page content.
- `{{ result }}` – Displays the result received from Python.

## 4. Adding URL Routing

Open `calc/urls.py` and add a new URL path.

**calc/urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
]
```

### Explanation

- `path('add', views.add, name='add')` connects the `add` URL to the `add()` view function.
- When the user submits the form, Django calls the `add()` function.

## 5. Creating the Addition Function in views.py

Open `calc/views.py` and write the following code.

**calc/views.py**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])

    res = val1 + val2

    return render(request, 'result.html', {'result': res})
```

### Explanation

| Code | Purpose |
|---|---|
| `request.GET["num1"]` | Gets the first number from the form |
| `request.GET["num2"]` | Gets the second number from the form |
| `int()` | Converts the input string into an integer |
| `val1 + val2` | Adds the two numbers |
| `render()` | Displays the result HTML page |
| `{'result': res}` | Sends the result to the HTML page |

**Important:** HTML form values are received as strings. We use `int()` to convert them into integers before performing addition.

## 6. Run the Django Server

Open CMD inside your Django project directory.

Activate the virtual environment if it is not already active:

```cmd
workon AS
```

Run the server:

```cmd
python manage.py runserver
```

Open this URL in your browser:

```text
http://127.0.0.1:8000/
```

## 7. Expected Output

### Home Page

```text
Addition of Two Numbers

Enter First Number:  20

Enter Second Number:  30

              [Add]
```

### Result Page

```text
Addition Result

Result: 50
```

## 8. How It Works

```text
        User Opens Website
                |
                v
           home.html
                |
                v
       Enter Two Numbers
                |
                v
          Submit Form
                |
                v
         calc/urls.py
                |
                v
          views.add()
                |
                v
       request.GET["num1"]
       request.GET["num2"]
                |
                v
        Convert into int()
                |
                v
          Add Two Numbers
                |
                v
          result.html
                |
                v
        Display Final Result
```

## 9. Important Django Topics Learned

| Topic | Meaning |
|---|---|
| HTML Forms | Used to collect input from users |
| Form Action | Specifies where form data is submitted |
| GET Method | Sends form data through the URL |
| `request.GET` | Accesses data submitted using GET |
| Type Conversion | Converts strings into integers |
| URL Routing | Connects URLs to view functions |
| View Function | Handles user requests and application logic |
| Context Dictionary | Sends Python data to HTML |
| Dynamic Content | Displays Python values inside HTML |

## 10. Practice Tasks

Try these tasks yourself:

1. Create a program to subtract two numbers.
2. Create a program to multiply two numbers.
3. Create a program to divide two numbers.
4. Display all four operations on the result page.

## 11. What I Learned Today

- How to create HTML forms.
- How to collect user input.
- How to use the GET method.
- How to access form data using `request.GET`.
- How to convert strings into integers.
- How to perform calculations in Django views.
- How to pass results from Python to HTML.
- How to display results on another HTML page.

**Day 4 completed – Successfully created a Django application that takes two numbers from the user and displays their sum!** 🚀

# Day 5 – POST Method and CSRF Protection in Django

**Date:** 01 November 2026

## 1. What I Learned Today

Today, I learned:
- Difference between GET and POST methods.
- How to send form data using the POST method.
- How to hide form data from the browser address bar.
- What is CSRF protection in Django?
- How to use `{% csrf_token %}` in HTML forms.
- How to access POST data using `request.POST`.

## 2. Difference Between GET and POST Methods

In Django, GET and POST are two HTTP methods used to send data between the browser and the server.

### GET Method

- GET is used to request data from the server.
- Form data is sent through the URL.
- Data is visible in the browser address bar.
- It is commonly used for searching and filtering.

**Example URL:**

```text
http://127.0.0.1:8000/add?num1=4&num2=4
```

Here, `num1=4` and `num2=4` are visible in the URL.

### POST Method

- POST is used to send data to the server.
- Form data is sent in the request body.
- Form data does not appear in the URL.
- It is commonly used for submitting forms and saving data.

**Important:** POST hides form values from the address bar, but it does not automatically encrypt or secure the data. HTTPS is needed to protect data while it travels between the browser and server.

## 3. Changing GET Method to POST Method

Previously, I used the GET method to add two numbers.

Now, I changed the form to use the POST method.

### Step 1: Update home.html

Open `home.html` and update the form.

```html
{% extends 'base.html' %}

{% block content %}

<h1>Addition of Two Numbers</h1>

<form action="add" method="post">

    {% csrf_token %}

    Enter First Number:
    <input type="text" name="num1"><br><br>

    Enter Second Number:
    <input type="text" name="num2"><br><br>

    <input type="submit" value="Add">

</form>

{% endblock %}
```

### Explanation

- `method="post"` – Sends form data using the POST method.
- `{% csrf_token %}` – Adds a CSRF security token to the form.
- `name="num1"` – Identifies the first input value.
- `name="num2"` – Identifies the second input value.

## 4. What is CSRF?

CSRF stands for **Cross-Site Request Forgery**.

It is a type of attack where an attacker tries to make a user perform an unwanted action on a website without their knowledge.

Django provides built-in CSRF protection to help prevent these attacks.

### Why did I get the CSRF error?

When I changed the form method from GET to POST, I received this error:

```text
CSRF verification failed. Request aborted.
```

This happened because Django checks POST requests for a valid CSRF token.

### How did I fix the error?

I added this template tag inside the HTML form:

```html
{% csrf_token %}
```

Django automatically generates and adds the required CSRF token.

**Important:** Always place `{% csrf_token %}` inside the POST form when using Django's CSRF protection.

## 5. Updating views.py

Previously, I used `request.GET` to receive form data.

Now, I changed it to `request.POST`.

Open `calc/views.py`:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    res = val1 + val2

    return render(request, 'result.html', {'result': res})
```

### Explanation

| Code | Purpose |
|---|---|
| `request.GET` | Gets data sent using GET |
| `request.POST` | Gets data sent using POST |
| `request.POST['num1']` | Gets the first number |
| `request.POST['num2']` | Gets the second number |
| `int()` | Converts string into integer |
| `val1 + val2` | Adds the two numbers |
| `render()` | Displays the result page |

## 6. Run the Django Server

Open CMD inside your Django project directory.

Activate the virtual environment:

```cmd
workon AS
```

Start the server:

```cmd
python manage.py runserver
```

Open the browser:

```text
http://127.0.0.1:8000/
```

Enter two numbers and click the Add button.

### Expected Output

**Input:**

```text
First Number: 4
Second Number: 4
```

**Result:**

```text
Addition Result

Result: 8
```

Notice that the numbers are not displayed in the browser address bar when using POST.

## 7. GET vs POST – Quick Revision

| GET | POST |
|---|---|
| Sends data through URL parameters | Sends data in the request body |
| Data is visible in the URL | Form values are not shown in the URL |
| Can be bookmarked with its parameters | Cannot be bookmarked with submitted form data in the same way |
| Commonly used for searching | Commonly used for submitting forms |
| Access data using `request.GET` | Access data using `request.POST` |

## 8. Important Concepts Learned Today

| Concept | Meaning |
|---|---|
| HTTP Methods | Methods used for communication between browser and server |
| GET | Used to request data |
| POST | Used to submit data |
| CSRF | Cross-Site Request Forgery |
| CSRF Token | Helps Django verify that a POST request comes from a valid form |
| `request.GET` | Accesses GET form data |
| `request.POST` | Accesses POST form data |
| HTTPS | Encrypts data while it travels between browser and server |

## 9. What I Learned Today

- How GET and POST methods work.
- How to change an HTML form from GET to POST.
- How POST sends data without displaying form values in the URL.
- Why Django gives a CSRF verification error.
- How to fix the CSRF error using `{% csrf_token %}`.
- How to receive POST data using `request.POST`.
- How to display the result on an HTML page.

**Day 5 completed – Successfully changed my Django form from GET to POST and learned about CSRF protection!** 🚀

# Day 6 – Session 2: Connecting External HTML Templates to Django

**Date:** 01 November 2026

## What I Learned

Today, I learned how to download an existing HTML template from a website and connect it to a Django project using a separate Django app.

We can use ready-made HTML templates instead of creating every HTML page from scratch.

## Step 1: Download an HTML Template

1. Open the [Colorlib website](https://colorlib.com/wp/templates/).
2. Choose a travel website template.
3. Download the template.
4. Extract the ZIP file.
5. Find the main HTML file, usually named `index.html`.

**Note:** A downloaded template may contain CSS, JavaScript, images, and other files. We need to keep these files in the correct folders so the website design works properly.

## Step 2: Create a New Django App

Open CMD and go to your Django project folder.

Activate your virtual environment:

```cmd
workon AS
```

Create a new app named `Travel`:

```cmd
python manage.py startapp Travel
```

Django creates a new folder named `Travel`.

## Step 3: Add the HTML File to Templates

Inside the `Travel` app, create a folder named `templates`.

Copy the downloaded `index.html` file into it.

Your folder structure should look like this:

```text
Travel/
│
├── migrations/
├── templates/
│   └── index.html
│
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

**Why do we create a templates folder?**

Django uses templates to display HTML pages in the browser.

## Step 4: Create urls.py Inside the Travel App

Django does not automatically create `urls.py` when we create an app. So, create it manually inside the `Travel` folder.

Add this code:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

**Explanation:**

- `path()` defines a URL.
- `views.index` connects the URL to the index view.
- `name='index'` gives a name to this URL.

## Step 5: Update views.py

Open `Travel/views.py` and add this code:

```python
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
```

**Explanation:**

- `render()` is used to display an HTML template.
- `index.html` is the HTML file inside the templates folder.
- `request` contains information about the browser request.

## Step 6: Connect the Travel App to the Main Project

Open the main project's `urls.py` file.

Import `include` and add the Travel app URL:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Travel.urls')),
    path('admin/', admin.site.urls),
]
```

**Explanation:**

`include('Travel.urls')` connects the main project URL to the Travel app URL.

When a user visits the website's home page, Django checks the Travel app's URL patterns and calls the `index` view.

**Important:** Make sure the app name and folder name match. Here, the app is named `Travel`, so use `Travel.urls`.

## Step 7: Run the Django Server

In CMD, run:

```cmd
python manage.py runserver
```

Open this URL in your browser:

```text
http://127.0.0.1:8000/
```

You should see your downloaded travel website's HTML page.

## Django Request Flow

```text
Browser
   |
   v
Main Project urls.py
   |
   v
Travel/urls.py
   |
   v
Travel/views.py
   |
   v
index.html
   |
   v
Browser displays the page
```

## Important Note: CSS, JavaScript and Images

If your HTML page opens but the design is missing, the CSS, JavaScript, or image files may not be connected.

We need to connect those files using Django static files.

We will use the static files setup learned in the previous session.

## Quick Revision

| File | Purpose |
|---|---|
| `Travel/urls.py` | Defines app URLs |
| `Travel/views.py` | Handles requests |
| `Travel/templates/index.html` | Contains the HTML page |
| Main project `urls.py` | Connects the Travel app |

## What I Learned Today

- How to download an external HTML template.
- How to create a new Django app.
- How to add an HTML file inside the templates folder.
- How to create `urls.py` manually.
- How to connect app URLs to the main project.
- How to display an external HTML page using `render()`.

## Practice Tasks

1. Download another HTML template from Colorlib.
2. Create a new Django app named `Portfolio`.
3. Add its `index.html` file inside the templates folder.
4. Create `urls.py` and `views.py`.
5. Connect the app to the main project.
6. Run the server and display the page.

**Today's Goal:** Learn how to reuse existing HTML templates in Django instead of creating every page from scratch.

# Day 6 – Connecting Static Files to Django

**Date:** 01 November 2026  
**Session:** 3

## 1. What are Static Files in Django?

Static files are files used to make a website look better and more attractive.

Examples of static files:

- CSS files – Used to add styles and colours.
- JavaScript files – Used to add actions and functionality.
- Images – Used to display pictures and logos.
- Fonts – Used to change text styles.

Django uses a special folder called `static` to manage these files.

## 2. Connecting Static Files to Django

### Step 1: Create a Static Folder

Inside the main Django project directory (the folder containing `manage.py`), create a folder named:

```text
static
```

### Step 2: Add External Static Files

Copy the required static files into the `static` folder.

For example:

```text
static/
│
├── css/
│   └── style.css
│
├── js/
│   └── script.js
│
└── images/
    └── logo.png
```

### Step 3: Update settings.py

Open `settings.py` in the main Django project folder.

Find the `STATIC_URL` setting and update it like this:

```python
import os

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
```

### Explanation

| Setting | Purpose |
|---|---|
| `STATIC_URL` | Defines the URL used to access static files |
| `STATICFILES_DIRS` | Tells Django where to find static files during development |
| `STATIC_ROOT` | Defines the folder where collected static files are stored |

**Note:** `STATICFILES_DIRS` and `STATIC_ROOT` have different purposes. Do not use the same folder for both.

### Step 4: Collect Static Files

Open CMD inside your Django project directory.

Activate the virtual environment:

```cmd
workon AS
```

Run the following command:

```cmd
python manage.py collectstatic
```

This command collects static files from the different static folders and copies them into the folder specified by `STATIC_ROOT`.

In my project, the collected files are stored inside the `assets` folder.

**Note:** `collectstatic` is mainly used when preparing a Django project for deployment. During local development with `DEBUG = True`, Django can normally serve static files directly without running this command every time.

### Step 5: Connect Static Files in HTML

Open your HTML file, for example `home.html` or `index.html`.

First, add this line at the top of the HTML file:

```django
{% load static %}
```

This loads Django's static template tag.

Now, update the paths of CSS, JavaScript and image files.

**Example: Connecting CSS**

```html
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

**Example: Connecting JavaScript**

```html
<script src="{% static 'js/script.js' %}"></script>
```

**Example: Connecting an Image**

```html
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

We can use `{% static %}` to connect different static files wherever required in the HTML page.

### Step 6: Run the Django Server

Open CMD and run:

```cmd
python manage.py runserver
```

Open the browser:

```text
http://127.0.0.1:8000/
```

Now the CSS, JavaScript and image files should load in the browser if their paths and settings are correct.

## 3. How Static Files Work in Django

```text
          Django Project
                |
                v
           settings.py
                |
                v
          STATICFILES_DIRS
                |
                v
           static folder
          /     |      \
         v      v       v
        CSS    JS     Images
          \     |      /
                |
                v
          HTML Template
                |
                v
          Browser Output
```

## 4. Important Django Static File Commands and Syntax

| Command / Syntax | Purpose |
|---|---|
| `STATIC_URL` | Defines the static file URL |
| `STATICFILES_DIRS` | Defines additional static file locations |
| `STATIC_ROOT` | Defines the collection destination |
| `python manage.py collectstatic` | Collects static files |
| `{% load static %}` | Loads the static template tag |
| `{% static 'css/style.css' %}` | Connects a CSS file |
| `{% static 'js/script.js' %}` | Connects a JavaScript file |
| `{% static 'images/logo.png' %}` | Connects an image |

## 5. What I Learned Today

- What static files are in Django.
- How to create a static folder.
- How to add CSS, JavaScript and image files.
- How to configure static file settings in `settings.py`.
- Difference between `STATIC_URL`, `STATICFILES_DIRS` and `STATIC_ROOT`.
- How to use the `collectstatic` command.
- How to load static files inside HTML using `{% load static %}`.
- How to connect CSS, JavaScript and images using `{% static %}`.

**Day 6 completed – Successfully learned how to connect static files to Django HTML templates!** 🚀

# 02/11/2026 – Django Session 3
## Topic: Passing Dynamic Data into HTML

### Part 1: Passing Dynamic Data from Views to HTML

**Step 1: Open `views.py`**

Use the `render()` function to pass data from Python to an HTML file.

```python
def index(request):
    return render(request, "index.html", {'prise': 400})
```

Here:
- `index.html` – HTML template file.
- `prise` – Variable name.
- `400` – Value passed from Python to HTML.

**Step 2: Open `index.html`**

Use Django Template Language to display the value.

```html
<div class="prise">
    {{ prise }}
</div>
```

**Step 3: Refresh the browser**

The output will display:

```text
400
```

---

### Part 2: Passing Model Objects into HTML

In this part, we create a model class and pass its object from the view to the HTML template.

**Step 1: Open `models.py`**

Create a Django model.

```python
from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()
```

Explanation:

- `models.Model` – Makes this class a Django database model.
- `name` – Stores the destination name.
- `img` – Stores the image path.
- `desc` – Stores the destination description.
- `price` – Stores the destination price.

**Step 2: Open `views.py`**

Import the model and create an object.

```python
from .models import Destination

def index(request):

    dest1 = Destination()
    dest1.name = 'Bengaluru'
    dest1.desc = 'The city is never sleep'
    dest1.price = 800

    return render(request, "index.html", {'dest1': dest1})
```

Here:
- `Destination()` – Creates a model object.
- `dest1.name` – Assigns the destination name.
- `dest1.desc` – Assigns the description.
- `dest1.price` – Assigns the price.
- `{'dest1': dest1}` – Passes the object to the HTML template.

**Step 3: Open `index.html`**

Display the object's values using Django Template Language.

```html
<a href="destination_details.html">
    <h3>{{ dest1.name }}</h3>
</a>

<p>{{ dest1.desc }}</p>

<p>{{ dest1.price }}</p>
```

**Expected output:**

```text
Bengaluru
The city is never sleep
800
```

---

### Important Points to Remember

1. `render()` is used to send data from views to HTML.
2. `{{ variable }}` displays a variable in an HTML template.
3. Django models are created inside `models.py`.
4. `models.Model` is used as the parent class for Django models.
5. We use dot notation to access object attributes in HTML, such as `{{ dest1.name }}`.
6. The dictionary key in `render()` must match the variable name used in HTML.

### Practice Task

Create another destination object:

- Name: Mumbai
- Description: Financial capital of India
- Price: 1200

Display its name, description and price in `index.html`.
