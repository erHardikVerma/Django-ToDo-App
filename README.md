# 📝 Django ToDo App

A beginner-friendly To-Do List application built with Django and Django REST Framework. Includes both a frontend and REST API.

---

## 🔧 Features

- Create, Read, Update, Delete (CRUD) tasks
- Mark tasks as completed or pending
- REST API endpoints for full control
- Admin panel for managing tasks
- Clean browser UI with checkboxes and delete buttons

---

## 📦 Tech Stack

- Python 3.12
- Django 5.2
- Django REST Framework
- SQLite3 (default)

---

## 🚀 Getting Started Locally

```bash
git clone https://github.com/erHardikVerma/Django-ToDo-App.git
cd Django-ToDo-App
python -m venv env
env\Scripts\activate   # On Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## 📡 API Endpoints

| Method | URL                         | Description        |
|--------|-----------------------------|--------------------|
| GET    | `/api/`                     | API Overview       |
| GET    | `/api/task-list/`           | Get all tasks      |
| GET    | `/api/task-detail/<id>/`    | Get single task    |
| POST   | `/api/task-create/`         | Create task        |
| POST   | `/api/task-update/<id>/`    | Update task        |
| DELETE | `/api/task-delete/<id>/`    | Delete task        |

---

## ✍️ Author

**Hardik Verma**  
GitHub: [@erHardikVerma](https://github.com/erHardikVerma)

