# How to Run — Task Management System

Two ways to run this project: **Docker** (recommended, one command) or **Local** (manual setup).

---

## Option 1 — Docker (Recommended)

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

### Steps

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd user_task_fastapi
```

**2. Start all containers**
```bash
docker compose up --build
```

This starts three containers automatically:
- PostgreSQL database on port `5432`
- FastAPI backend on port `8000`
- React frontend on port `5173`

Wait until you see `Uvicorn running on http://0.0.0.0:8000` in the logs.

**3. Seed the admin user** (open a new terminal)
```bash
docker compose exec backend python seed.py
```

Output:
```
[seed] Admin user created successfully
       Email    : admin@example.com
       Password : admin123
       Role     : admin
```

**4. Open the app**

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |

**5. Stop the containers**
```bash
docker compose down
```

---

## Option 2 — Local Setup (Manual)

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL installed and running

---

### Backend Setup

**1. Navigate to the backend folder**
```bash
cd backend
```

**2. Create and activate a virtual environment**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac / Linux:
```bash
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create the `.env` file**

Copy the example file:
```bash
cp .env.example .env
```

Then open `.env` and fill in your values:
```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/task_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> Make sure the PostgreSQL database (`task_db`) exists before running.
> Create it via psql or pgAdmin if needed:
> ```sql
> CREATE DATABASE task_db;
> ```

**5. Start the backend**
```bash
uvicorn app.main:app --reload
```

Backend is now running at `http://localhost:8000`

**6. Seed the admin user** (in the same terminal or a new one with venv active)
```bash
python seed.py
```

Output:
```
[seed] Admin user created successfully
       Email    : admin@example.com
       Password : admin123
       Role     : admin
```

---

### Frontend Setup

**1. Open a new terminal and navigate to the frontend folder**
```bash
cd frontend
```

**2. Install dependencies**
```bash
npm install
```

**3. Start the frontend**
```bash
npm run dev
```

Frontend is now running at `http://localhost:5173`

---

## Credentials

### Admin Login
```
Email    : admin@example.com
Password : admin123
```

### Regular User
Register a new account from the `/register` page.

---

## API Documentation

Interactive Swagger UI is available at:
```
http://localhost:8000/docs
```

You can test all endpoints directly from the browser:
1. Register or log in to get a JWT token
2. Click **Authorize** and paste the token
3. Make authenticated requests

---

## Project URLs Summary

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |
| Register | http://localhost:5173/register |
| Login | http://localhost:5173/login |
| Dashboard | http://localhost:5173 |
| Admin Panel | http://localhost:5173/admin |
