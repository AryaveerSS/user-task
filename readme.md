# Full Stack Task Management System

A production-style full-stack task management application built using FastAPI, React, PostgreSQL, JWT Authentication, Docker, and Role-Based Access Control (RBAC).

The system supports secure authentication, task management, admin controls, Docker deployment, and logging.

---

## Features

### Authentication & Security

- User Registration
- User Login
- JWT Authentication
- Password Hashing (bcrypt)
- Protected API Routes
- Protected Frontend Routes
- Persistent Login Sessions
- Role-Based Access Control (RBAC)
- Admin Authorization
- Input Validation
- Secure Password Storage

---

### Task Management

Users can:

- Create Tasks
- View Tasks
- Edit Tasks
- Delete Tasks
- Update Task Status
- Toggle Completion State

---

### Admin Dashboard

Admin users can:

- View All Users
- View All Tasks
- Delete Any User
- Delete Any Task
- Manage Platform Data

---

### Error Handling

Frontend displays:

- Invalid Password
- Short Password Validation
- Duplicate Email Detection
- Login Failure Messages
- Registration Errors
- API Validation Errors

Backend handles:

- HTTP Exceptions
- Validation Errors
- Authentication Errors
- Authorization Errors

---

### Logging System

Application logs:

- User Registration
- User Login
- Failed Login Attempts
- Task Creation
- Task Updates
- Task Deletion
- Admin Actions

Example:

```
2026-05-20 INFO user@gmail.com logged in

2026-05-20 INFO Task created: Build Backend API

2026-05-20 WARNING Admin deleted user
```

---

## Docker Support

Application is fully containerized.

Docker containers:

- Frontend Container
- Backend Container
- PostgreSQL Container

Start project:

```bash
docker compose up --build
```

Stop:

```bash
docker compose down
```

---

## Tech Stack

### Backend

- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Pydantic
- JWT Authentication
- Passlib
- bcrypt
- Python Logging

### Frontend

- React
- Vite
- Axios
- React Router DOM

### DevOps

- Docker
- Docker Compose

---

## Project Structure

```

project-root/

├── backend/
│
├── app/
│ ├── admin/
│ ├── core/
│ ├── tasks/
│ ├── users/
│ ├── utils/
│ └── main.py
│
├── requirements.txt
├── Dockerfile
└── .env

├── frontend/
│
├── src/
│ ├── context/
│ ├── pages/
│ ├── routes/
│ ├── services/
│ └── components/
│
├── package.json
├── Dockerfile
└── vite.config.js

├── docker-compose.yml

└── README.md

```

---

## Installation (Local)

### Backend

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Create `.env`

```

DATABASE_URL=postgresql://username:password@localhost/database

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend:

```

http://localhost:8000

```

---

### Frontend

Move frontend:

```bash
cd frontend
```

Install:

```bash
npm install
```

Run:

```bash
npm run dev
```

Frontend:

```

http://localhost:5173

```

---

## Docker Setup

Run:

```bash
docker compose up --build
```

Frontend:

```

http://localhost:5173

```

Backend:

```

http://localhost:8000/docs

```

---

## API Endpoints

### Authentication

| Method | Endpoint |
|----------|--------------------------|
| POST | /api/v1/users/register |
| POST | /api/v1/users/login |
| GET | /api/v1/users/me |

---

### Tasks

| Method | Endpoint |
|----------|---------------------|
| GET | /api/v1/tasks |
| POST | /api/v1/tasks |
| PUT | /api/v1/tasks/{id} |
| DELETE | /api/v1/tasks/{id} |

---

### Admin

| Method | Endpoint |
|----------|---------------------------|
| GET | /api/v1/admin/users |
| GET | /api/v1/admin/tasks |
| DELETE | /api/v1/admin/users/{id} |
| DELETE | /api/v1/admin/tasks/{id} |

---

## Security Features

- JWT Authentication
- Password Hashing
- Protected Routes
- Role-Based Access Control
- Admin Authorization
- Validation Layer
- Secure Token Management

---

## Future Improvements

- Task Filtering
- Pagination
- Redis Caching
- Unit Testing
- CI/CD Pipeline
- Email Verification
- Profile Management
- Notifications

---

## Screenshots

Add:

- Login Page
- Register Page
- Dashboard
- Admin Dashboard

---

## Author

Aryaveer Singh

Backend Developer | FastAPI | PostgreSQL | React
