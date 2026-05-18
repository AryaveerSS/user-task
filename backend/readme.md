# Scalable Task Management API

A production-style backend application built with FastAPI, PostgreSQL, JWT Authentication, and Role-Based Access Control (RBAC). The project includes a simple React frontend for interacting with the APIs.

## Features

### Authentication & Authorization
- User Registration
- User Login
- Password Hashing using BCrypt
- JWT Authentication
- Protected Routes
- Role-Based Access Control (User/Admin)

### Task Management
- Create Tasks
- Get Tasks
- Update Tasks
- Delete Tasks
- User-specific task ownership

### Backend Features
- FastAPI REST APIs
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Pydantic Validation
- API Versioning
- Modular Scalable Architecture
- Error Handling
- Swagger Documentation

### Frontend Features
- User Registration/Login UI
- Protected Dashboard
- CRUD Operations for Tasks
- API Integration using Axios

---

# Tech Stack

## Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Passlib (BCrypt)

## Frontend
- React.js
- Axios
- Tailwind CSS

---

# Project Structure

```bash
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │
│   ├── users/
│   │   ├── model.py
│   │   ├── schema.py
│   │   ├── router.py
│   │   ├── service.py
│   │   ├── dependencies.py
│   │
│   ├── tasks/
│   │   ├── model.py
│   │   ├── schema.py
│   │   ├── router.py
│   │   ├── service.py
│   │
│   ├── utils/
│   │   ├── hashing.py
│   │   ├── jwt_handler.py
│   │
│   └── middleware/
│       └── error_handler.py
│
├── requirements.txt
├── .env
└── README.md