# DJANGO REST FRAMEWORK (DRF) TUTORIAL

## Topics/steps

1. [What is django](#what-is-django)
1. [Start project](#start-project)
1. [What is an app??](#what-is-an-app)
1. [Start app, installing app.](#start-app-installing-app)
1. [What is a model??](#what-is-a-model)
1. [First model](#first-model)
1. [Playing with the models](#playing-with-the-models)
1. [Improving models](#improving-models)
1. [Create admin](#create-admin)
1. [Where come DRF?](#where-come-drf)
1. [DRF Parts](#drf-parts)
1. [First view!!](#first-view)

## git tag

You can easily go to the next step following the correponding tag

|tag|step|
|:--:|:--|
|v0.0|            Initial version|
|v0.1|            Setup project|
|v0.2|            First app|
|v0.3|            Installing academy app|
|v0.4|            First models|
|v0.5|            First migrations|
|v0.6|            Creating the admin|
|v1.0|            First view!|

```bash
git checkout v0.3
```

___
## What is django??

#### Django makes it easier to build better Web apps more quickly and with less code.

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

*Ridiculously fast.*

Django was designed to help developers take applications from concept to completion as quickly as possible.|


*Reassuringly secure.*

Django takes security seriously and helps developers avoid many common security mistakes.


*Exceedingly scalable.*

Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

[djangoproject.com](https://www.djangoproject.com/)

---

## Start project

```bash
python -m pip install -r requirements.txt
```
```bash
python -m django startproject Tutorials
```

    Tutorials:.
    │   .gitignore
    │   manage.py
    │   README.md
    │   requirements.txt
    │
    └───Tutorials
            settings.py
            urls.py
            wsgi.py
            __init__.py

## What is an app??

The term application describes a Python package that provides some set of features. Applications may be reused in various projects.

Applications include some combination of models, views, templates, template tags, static files, URLs, middleware, etc. They’re generally wired into projects with the INSTALLED_APPS setting and optionally with other mechanisms such as URLconfs, the MIDDLEWARE setting, or template inheritance.

[applications](https://docs.djangoproject.com/en/3.0/ref/applications/)

---

## Start app, installing app.

```bash
python manage.py startapp academy
```

    Tutorials:.
        │   .gitignore
        │   manage.py
        │   README.md
        │   requirements.txt
        |
        ├───academy
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   └───migrations
        │           __init__.py
        └───Tutorials
                settings.py
                urls.py
                wsgi.py
                __init__.py

add ``academy`` and another apps to ``INSTALLED_APPS`` into [settings.py](Tutorials/settings.py)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'django_extensions',
    'django_filters',
    'academy',
]
```


## What is a model??

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

The basics:

Each model is a Python class that subclasses ``django.db.models.Model``.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API;

[models](https://docs.djangoproject.com/en/3.0/topics/db/models/)

---
## First model

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

    Tutorials:.
    │   .gitignore
    |   db.sqlite3
    │   manage.py
    │   README.md
    │   requirements.txt
    │
    ├───academy
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   tests.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   └───migrations
    │           0001_initial.py
    │           __init__.py
    │
    └───Tutorials
            settings.py
            urls.py
            wsgi.py
            __init__.py

## Playing with the models

```bash
python manage.py shell
>>> from academy import models
>>> react = models.Topic.objects.create(name="React")
>>> react
<Topic: Topic object (1)>
>>> 
>>> react101 = models.Course.objects.create(topic=react,name="101", description="Awesome description")
>>> react101
<Course: Course object (1)>
>>> models.Course.objects.create(topic=react,name="202", description="Awesome description")
>>>
>>> react.course_set.all()
<QuerySet [<Course: Course object (1)>, <Course: Course object (2)>]>
>>> 
>>> react.course_set.filter(name="101")
<QuerySet [<Course: Course object (1)>]>
>>> 
>>> models.Course.objects.filter(topic__name="React")
<QuerySet [<Course: Course object (1)>, <Course: Course object (2)>]>
>>> 
>>> models.Course.objects.filter(topic=react)
<QuerySet [<Course: Course object (1)>, <Course: Course object (2)>]>

```

## Improving models

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

    Tutorials:.
    │   .gitignore
    |   db.sqlite3
    │   manage.py
    │   README.md
    │   requirements.txt
    │
    ├───academy
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   tests.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   └───migrations
    │           0001_initial.py
    │           0002_auto_20200402_1646.py
    │           __init__.py
    │
    └───Tutorials
            settings.py
            urls.py
            wsgi.py
            __init__.py

## Create admin

```bash
python manage.py create createsuperuser
```
```bash
python manage.py admin_generator academy
# or
python manage.py admin_generator academy > academy/admin.py
```

## Where come DRF?

#### Django REST framework is a powerful and flexible toolkit for building Web APIs.

___
Django Rest Framework makes it easy to use your Django Server as an REST API.

REST stands for "representational state transfer" and API stands for application programming interface.

You can build a restful api using regular Django, but it will be very tidious. DRF makes everything easy.

---

Some reasons you might want to use REST framework:

* The Web browsable API is a huge usability win for your developers.
* Authentication policies including packages for OAuth1a and OAuth2.
* Serialization that supports both ORM and non-ORM data sources.
* Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
* Extensive documentation, and great community support.
Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

[django-rest-framework](https://www.django-rest-framework.org/)

---

## DRF Parts

There are more, a lot more, but simplifying:

1. Serializers

    Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

    [serializers](https://www.django-rest-framework.org/api-guide/serializers/)
    
1. Views

    Views are responsible for receiving clients requests and responding with the requested data.

    [1. Class-based / Functions-based views](https://www.django-rest-framework.org/api-guide/views/)

    [1. Generic-views](https://www.django-rest-framework.org/api-guide/generic-views/)

    [1. Viewsets](https://www.django-rest-framework.org/api-guide/viewsets/)

1. Urls (Routers)

    Routers are in charge of organizing views into like path structure.

    [see more](https://www.django-rest-framework.org/api-guide/routers/)
        

## View types
1. ~~2~~ Class-based Views

    ```python
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import authentication, permissions
    from django.contrib.auth.models import User

    class ListUsers(APIView):
        """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
        """
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]

        def get(self, request, format=None):
            """
            Return a list of all users.
            """
            usernames = [user.username for user in User.objects.all()]
            return Response(usernames)
    ```

1. ~~1~~ Functions based view

    ```python
    from rest_framework.decorators import api_view

    @api_view(['GET', 'POST'])
    def hello_world(request):
        if request.method == 'POST':
            return Response({"message": "Got some data!", "data": request.data})
        return Response({"message": "Hello, world!"})
    ```
    ```bash
    python manage.py create createsuperuser
    ```

1. Generic and mixin views
    
    ```python
    from django.contrib.auth.models import User
    from myapp.serializers import UserSerializer
    from rest_framework import generics
    from rest_framework.permissions import IsAdminUser

    class UserList(generics.ListCreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        permission_classes = [IsAdminUser]
    ```

    ---
    
    #### CreateAPIView
    Used for *create-only* endpoints.

    Provides a ``post`` method handler.

    Extends: ```GenericAPIView```, ```CreateModelMixin```

    ---
    
    #### ListAPIView
    Used for *read-only* endpoints to represent a collection of model instances.

    Provides a ``get`` method handler.

    Extends: ```GenericAPIView```, ```ListModelMixin```

    ---
    
    #### RetrieveAPIView
    Used for *read-only* endpoints to represent a single model instance.

    Provides a ``get`` method handler.

    Extends: ```GenericAPIView```, ```RetrieveModelMixin```

    ---
    
    #### DestroyAPIView
    Used for *delete-only* endpoints for a single model instance.

    Provides a ``delete`` method handler.

    Extends: ```GenericAPIView```, ```DestroyModelMixin```

    ---
    
    #### UpdateAPIView
    Used for *update-only* endpoints for a single model instance.

    Provides ``put`` and ``patch`` method handlers.

    Extends: ```GenericAPIView```, ```UpdateModelMixin```

    ---
    
    #### ListCreateAPIView
    Used for *read-write* endpoints to represent a collection of model instances.

    Provides ``get`` and ``post`` method handlers.

    Extends: ```GenericAPIView```, ```ListModelMixin```, ```CreateModelMixin```

    ---
    
    #### RetrieveUpdateAPIView
    Used for *read* or *update* endpoints to represent a single model instance.

    Provides ``get``, ``put`` and ``patch`` method handlers.

    Extends: ```GenericAPIView```, ```RetrieveModelMixin```, ```UpdateModelMixin```

    ---
    
    #### RetrieveDestroyAPIView
    Used for *read* or *delete* endpoints to represent a single model instance.

    Provides ``get`` and ``delete`` method handlers.

    Extends: ```GenericAPIView```, ```RetrieveModelMixin```, ```DestroyModelMixin```

    ---
    
    #### RetrieveUpdateDestroyAPIView
    Used for *read-write-delete* endpoints to represent a single model instance.

    Provides ``get``, ``put``, ``patch`` and ``delete`` method handlers.

    Extends: ```GenericAPIView```, ```RetrieveModelMixin```, ```UpdateModelMixin```, ```DestroyModelMixin```

1. Viewsets

    The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, by mixing in the behavior of the various mixin classes.

    The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().
    
    ```python
    class UserViewSet(viewsets.ModelViewSet):
        """
        A viewset for viewing and editing user instances.
        """
        serializer_class = UserSerializer
        queryset = User.objects.all()
    ```
 
## First view!!

    Tutorials:.
    │   .gitignore
    |   db.sqlite3
    │   manage.py
    │   README.md
    │   requirements.txt
    │
    ├───academy
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   serializers.py
    │   │   tests.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   └───migrations
    │           0001_initial.py
    │           0002_auto_20200402_1646.py
    │           __init__.py
    │
    └───Tutorials
            settings.py
            urls.py
            wsgi.py
            __init__.py

