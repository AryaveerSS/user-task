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