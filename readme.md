# README.md

````md id="r4n8x1"
# Full Stack Task Management System

A full-stack task management application built using FastAPI, PostgreSQL, React, and JWT Authentication with Role-Based Access Control (RBAC).

---

# Features

## Authentication
- User Registration
- User Login
- JWT Authentication
- Password Hashing using bcrypt
- Protected Routes
- Persistent Login

---

## Task Management
- Create Tasks
- View Tasks
- Update Tasks
- Delete Tasks
- Toggle Task Completion Status

---

## Admin Features
- View All Users
- View All Tasks
- Delete Any User
- Delete Any Task
- Role-Based Access Control (RBAC)

---

# Tech Stack

## Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Passlib / bcrypt

---

## Frontend
- React
- Vite
- Axios
- React Router DOM

---

# Project Structure

```bash
project-root/
│
├── backend/
│
│   ├── app/
│   │
│   │   ├── admin/
│   │   ├── core/
│   │   ├── tasks/
│   │   ├── users/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│
│   ├── src/
│   │
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   ├── routes/
│   │   └── services/
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
````

---

# Backend Setup

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create `.env`

```env
DATABASE_URL=postgresql://postgres:password@localhost/task_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 6. Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

## 1. Move To Frontend Folder

```bash
cd frontend
```

---

## 2. Install Dependencies

```bash
npm install
```

---

## 3. Start Frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# API Endpoints

## Authentication

| Method | Endpoint               |
| ------ | ---------------------- |
| POST   | /api/v1/users/register |
| POST   | /api/v1/users/login    |

---

## Tasks

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | /api/v1/tasks      |
| POST   | /api/v1/tasks      |
| PUT    | /api/v1/tasks/{id} |
| DELETE | /api/v1/tasks/{id} |

---

## Admin

| Method | Endpoint                 |
| ------ | ------------------------ |
| GET    | /api/v1/admin/users      |
| GET    | /api/v1/admin/tasks      |
| DELETE | /api/v1/admin/users/{id} |
| DELETE | /api/v1/admin/tasks/{id} |

---

# Security Features

* JWT Authentication
* Password Hashing
* Protected Routes
* Role-Based Authorization
* Admin Route Protection
* Input Validation
* Error Handling

---

# Future Improvements

* Task Search & Filtering
* Pagination
* Docker Support
* Task Deadlines
* Email Verification
* Deployment
* Unit Testing

---

# Author

Aryaveer Singh

```
```
