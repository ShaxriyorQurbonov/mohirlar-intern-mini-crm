# mohirlar-intern-mini-crm
Mini CRM backend built with Django REST Framework and PostgreSQL, featuring JWT authentication, lead management, filtering, searching, pagination, and status tracking.

# Mini CRM

A small CRM backend for managing leads, built with Django REST Framework.

## Features

- User registration
- JWT authentication
- Lead CRUD operations
- Lead status management
- Lead ownership
- Search
- Filtering by status and source
- Ordering
- Pagination
- Input validation
- PostgreSQL database
- Swagger API documentation
- Automated API tests

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT
- django-filter
- drf-spectacular
- Git / GitHub

## Architecture

The project follows a simple Django REST Framework architecture.

```text
mohirlar_intern_task/
│
├── users/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── leads/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── mohirlar_intern_task/
│   ├── settings.py
│   └── urls.py
│
└── manage.py

## AI Usage

AI tools were used as a development assistant for:
- understanding Django REST Framework patterns;
- debugging validation and authentication issues;
- reviewing API architecture;
- generating initial test ideas.

All generated code was manually reviewed, tested, and adapted to the project requirements.