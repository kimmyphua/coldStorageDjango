
# Python Django Scrapping Lab

## Instructions
1. Clone this repository
1. Create a django project `django-admin startproject shoppingmall`
1. Create a django app `python manage.py startapp coldstorage`


## Set up Django app
1. Go to the project folder and add to the `settings.py` and register your django app name to the installed_app list
```python
  # Application definition

INSTALLED_APPS = [
    # local apps installed
    "coldstorage",
    # end of local apps installed
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```
1. Go to `urls.py` and add the baseurl for the app
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # add this line
    path("", include("coldstorage.urls"))  # routes for jobby app
]

```

1. In your `coldstorage folder` create a `urls.py` and add the following code to it
```python
from django.urls import path

from . import views # this is the views.py file within this directory

urlpatterns = [
    path("", views.index, name="index"),
    path("show/", views.show, name="show")
]

```

1. In your `coldstorage/views.py` add the following code.
```python

def index(request):
    render(request, "coldstorage/index.html")
```


1. Note you should create a `templates/coldstorage/index.html` to get started 
