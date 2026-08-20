# DailyDo – Todo App

A full-stack Todo application built to practice building a REST API with **Python, Flask, and SQLite**, and connecting it to a simple frontend using **HTML, CSS, and JavaScript**.

The project focuses on learning how a frontend communicates with a backend API, how CRUD operations work, and how filtering can be handled on the server side using query parameters.

## Features

- Add new todos
- View all todos
- View a single todo by ID
- Mark todos as completed or pending
- Edit todo titles
- Delete todos
- Filter todos by completion status
- Display pending and completed task counts
- SQLite database for persistent storage
- CORS enabled for frontend-backend communication

## Tech Stack

### Backend

- Python
- Flask
- Flask-CORS
- SQLite

### Frontend

- HTML
- CSS
- JavaScript
- Fetch API

## Project Structure

```text
29_todo_app_flask/
│
├── app.py                 # Flask application and API routes
├── models.py              # SQLite database operations
├── database.db            # SQLite database (created automatically)
├── README.md
│
└── frontend/
    ├── index.html         # Todo application UI
    ├── style.css          # Frontend styling
    └── script.js          # API calls and UI logic
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/todos` | Get all todos |
| GET | `/todos?completed=true` | Get completed todos |
| GET | `/todos?completed=false` | Get pending todos |
| GET | `/todos/<id>` | Get a todo by ID |
| POST | `/todos` | Create a new todo |
| PUT | `/todos/<id>` | Update a todo |
| DELETE | `/todos/<id>` | Delete a todo |

### Create a Todo

```http
POST /todos
Content-Type: application/json

{
  "title": "Learn Flask"
}
```

### Update a Todo

You can update the title or completion status.

```http
PUT /todos/1
Content-Type: application/json

{
  "completed": true
}
```

Or:

```http
PUT /todos/1
Content-Type: application/json

{
  "title": "Practice Flask APIs"
}
```

## Server-Side Filtering

One of the main learning goals of this project is understanding **query parameters** and server-side filtering.

For example:

```text
GET /todos?completed=true
```

returns only completed todos, while:

```text
GET /todos?completed=false
```

returns only pending todos.

The frontend sends the selected filter to the Flask backend, and the backend queries SQLite for the matching records.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/preethiangelin1/python-mini-projects.git
cd python-mini-projects/29_todo_app_flask
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask flask-cors
```

### 4. Start the Flask server

```bash
python3 app.py
```

The API will run at:

```text
http://127.0.0.1:5050
```

The SQLite database is initialized automatically when the Flask application starts.

### 5. Run the frontend

Open `frontend/index.html` in a browser, or serve the frontend directory using a local development server such as VS Code Live Server.

The frontend is configured to communicate with:

```text
http://127.0.0.1:5050/todos
```

Make sure the Flask backend is running before using the application.

## What I Learned

This project helped me practice:

- Building REST APIs with Flask
- Creating CRUD endpoints
- Working with SQLite using Python's `sqlite3` module
- Using HTTP methods: GET, POST, PUT, and DELETE
- Using query parameters for server-side filtering
- Connecting JavaScript to a Flask API using `fetch()`
- Handling JSON request and response data
- Enabling CORS in Flask
- Separating database logic from API routes
- Handling API errors and HTTP status codes
- Updating the UI based on API responses

## Future Improvements

Some ideas for extending the project:

- Add due dates and priorities
- Add user authentication
- Add pagination
- Add search functionality
- Add better form validation
- Deploy the backend and frontend
- Add automated tests with `pytest`

## Project Goal

This project is part of my Python learning journey, with a focus on moving from Python fundamentals to **backend API development with Flask**.

---

Built while learning Python backend development 🚀
