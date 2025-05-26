# 📝 Django ToDo App

A beginner-friendly To-Do List application built with Django and Django REST Framework. Includes both a browser-based frontend and REST API.

---

## 🔧 Features

- ✅ Create, Read, Update, Delete (CRUD) tasks  
- 🟢 Mark tasks as completed or pending  
- 🌐 REST API endpoints for external access (e.g., Postman)  
- 🔐 Admin panel to manage tasks  
- 🧼 Clean browser UI with checkboxes and delete buttons  

---

## 📦 Tech Stack

- Python 3.12  
- Django 5.2  
- Django REST Framework  
- SQLite3 (default database)  

---

## 🚀 Getting Started Locally

To run this project on your machine:

```bash
git clone https://github.com/erHardikVerma/Django-ToDo-App.git
cd Django-ToDo-App
python -m venv env
env\Scripts\activate   # On Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then visit: `http://127.0.0.1:8000`

---

## 📡 API Endpoints

| Method | URL                          | Description         |
|--------|------------------------------|---------------------|
| GET    | `/api/`                      | API Overview        |
| GET    | `/api/task-list/`            | List all tasks      |
| GET    | `/api/task-detail/<id>/`     | Get task by ID      |
| POST   | `/api/task-create/`          | Create a new task   |
| POST   | `/api/task-update/<id>/`     | Update a task       |
| DELETE | `/api/task-delete/<id>/`     | Delete a task       |

---

## ✍️ Author

**Hardik Verma**  
GitHub: [@erHardikVerma](https://github.com/erHardikVerma)

