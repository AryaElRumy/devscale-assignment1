# Student Data API

## Overview
This project is a basic CRUD (Create, Read, Update, Delete) application built with FastAPI for managing student data. It was developed as an assignment to demonstrate FastAPI implementation and Docker deployment skills.

## Features
- Complete CRUD operations for student records
- RESTful API design
- Database integration with SQLModel
- Database migrations using Alembic
- Docker containerization for easy deployment
- API documentation with Scalar

## Project Structure
```
├── app/                    # Main application directory
│   ├── database.py         # Database configuration and models
│   ├── main.py             # FastAPI application entry point
│   ├── routes/             # API route definitions
│   │   └── students.py     # Student-related endpoints
│   ├── schema.py           # Pydantic schemas for request/response models
│   └── setting.py          # Application settings
├── alembic/                # Database migration files
├── data/                   # Database storage
├── Dockerfile              # Docker configuration
├── makefile                # Development commands
├── pyproject.toml         # Project dependencies
└── README.md              # Project documentation
```

## API Endpoints

### Student Endpoints
- `GET /students/` - Get all students
- `GET /students/{student_id}` - Get a specific student by ID
- `POST /students/` - Register a new student
- `PUT /students/{student_id}` - Update a student's information
- `POST /students/{student_id}` - Unregister (delete) a student

### Other Endpoints
- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `GET /scalar` - API documentation

## Setup Instructions

### Prerequisites
- Python 3.7+
- uv package manager

### Local Development
1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Run database migrations:
   ```bash
   uv run alembic upgrade head
   ```
4. Start the development server:
   ```bash
   make dev
   ```
   or
   ```bash
   uv run uvicorn app.main:app --reload
   ```
5. Access the API at http://localhost:8000

## Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t student-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 student-api
   ```

3. Access the API at http://localhost:8000

## Code Formatting

To format the code according to project standards:
```bash
make format
```

## Database Schema

### Student
- `student_id`: Integer (Primary Key)
- `name`: String
- `grade`: Integer
- `address`: String

## Author
Mochamad Arya El Rumy

## License
This project is created for educational purposes as part of the AI-Enabled Bootcamp assignment.
