# Expense Tracker API

A robust backend API for an expense tracking application, built with Django and Django REST Framework. It provides
secure endpoints for user management, expense tracking, and data analysis.

## 📜 Table of Contents

- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [API Endpoints](#-api-endpoints)
- [Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation & Setup](#installation--setup)
- [Authentication](#-authentication)

## ✨ Key Features

- **User Authentication**: Secure user registration and login using JSON Web Tokens (JWT).
- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for expenses.
- **Expense Categorization**: Ability to create and assign categories to expenses.
- **Advanced Filtering**: Powerful filtering capabilities for expenses (e.g., by date range, category) using
  `django-filter`.
- **Scalable Architecture**: Built on Django, providing a solid and scalable foundation.
- **CORS Ready**: Pre-configured Cross-Origin Resource Sharing (CORS) for easy integration with frontend applications.

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (`psycopg2-binary`)
- **Authentication**: DRF Simple JWT (`djangorestframework_simplejwt`)
- **Environment Variables**: `django-environ`
- **API Filtering**: `django-filter`
- **CORS**: `django-cors-headers`

## 🔌 API Endpoints

Here is a summary of the available API endpoints.

| Endpoint                  |  Method  | Description                             | Protected |
|---------------------------|:--------:|-----------------------------------------|:---------:|
| `/api/v1/users/register/` |  `POST`  | Register a new user.                    |    No     |
| `/api/v1/token/`          |  `POST`  | Obtain JWT access and refresh tokens.   |    No     |
| `/api/v1token/refresh/`   |  `POST`  | Refresh an expired access token.        |    No     |
| `/api/v1/expenses/`       |  `GET`   | Get a list of the user's expenses.      |    Yes    |
| `/api/v1/expenses/`       |  `POST`  | Create a new expense.                   |    Yes    |
| `/api/v1/expenses/<id>/`  |  `GET`   | Retrieve a specific expense.            |    Yes    |
| `/api/v1/expenses/<id>/`  |  `PUT`   | Update a specific expense.              |    Yes    |
| `/api/v1/expenses/<id>/`  | `DELETE` | Delete a specific expense.              |    Yes    |
| `/api/v1/categories/`     |  `GET`   | Get a list of all available categories. |    Yes    |

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

- Python 3.8+
- Pip & a virtual environment tool (`venv`)
- A running instance of PostgreSQL

### Installation & Setup

1. **Clone the repository**
    - git clone https://github.com/IIFreddyII/expense_tracker.git
    - cd expense_tracker
2. **Create and activate a virtual environment**
    - (`python -m venv venv`)
    - Windows: (`venv\Scripts\activate`)
    - MacOS/Linux: (`source venv/bin/activate`)
3. **Install the dependencies**
    - (`pip install -r requirements.txt`)
4. **Configure environment variables**
    - Copy env example to (`core/.env`) and modify for local
5. **Run database migrations**
    - (`make migrate` or (`python manage.py migrate`))
6. **Create superuser**
    - (`make user` or (`python manage.py createsuperuser`)
7. **Run server**
    - (`make up` or (`python manage.py runserver`)

### 🔐 Authentication

This API is secured using JWT. To access secured endpoints, you must first obtain an access token.

1. **Send a POST request to /api/v1/token/ with your username and password.**
    - (`{"username": "your_username","password": "your_password"}`)
2. **The API will return an access token and a refresh token.**
    - (`{"access": "your_access_token","refresh": "your_refresh_token", "user": {}}`)
3. **Include the access token in the Authorization header of your subsequent requests as a "Bearer token."**
   - (`Authorization: Bearer <your_access_token>`)
