# 🎓 Django University Management System

## 📖 Project Overview

This project was developed as part of a Django assignment to demonstrate relational database modeling using the Django ORM (Object-Relational Mapper).

The goal is to build a simple university management system that manages students, professors, courses, semesters, student ID cards, and course descriptions.

The project demonstrates three types of database relationships:

- **One-to-One (1:1)**
- **One-to-Many (1:N)**
- **Many-to-Many (M:N)**

## 🛠️ Technologies Used

- Python
- Django 6.1.3
- SQLite
- Django ORM
- Django Admin

## 📂 Project Structure

```text
Django_Uni_Hausaufgabe/
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── university/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

The virtual environment and local SQLite database are excluded from version control.

## 🗃️ Database Models

The application contains six Django models.

### 1. Student
Stores student information, including name and unique email address.

### 2. Student ID Card
Stores a unique student ID number and connects each card to one student.

### 3. Professor
Stores professor names and their areas of expertise.

### 4. Semester
Represents an academic semester, such as Winter Semester 2026/2027.

### 5. Course
Stores course information and connects courses to professors, semesters, and students.

### 6. Course Description
Stores detailed information about a specific course.

## 🔗 Database Relationships

| Relationship | Type | Django Field |
|---|---|---|
| Student → Student ID Card | One-to-One | `OneToOneField` |
| Professor → Course | One-to-Many | `ForeignKey` |
| Semester → Course | One-to-Many | `ForeignKey` |
| Student ↔ Course | Many-to-Many | `ManyToManyField` |
| Course → Course Description | One-to-One | `OneToOneField` |

The one-to-one relationships prevent multiple ID cards per student and multiple descriptions per course. Additional validation would be required to ensure every student and course has its corresponding record.

## 🚀 Installation and Setup

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment (Windows)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create an Admin User

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open the Django Admin interface:

http://127.0.0.1:8000/admin/

## 🧪 Example Test Data

The following example records were created during development:

| Model | Example |
|---|---|
| Professor | Dr. Ahmad Ataya |
| Semester | Winter Semester 2026/2027 |
| Course | Django Fullstack Entwicklung |
| Student | Max Mustermann |
| Student ID Card | UNI-2026-001 |
| Course Description | Lernprojekt für Django Hausaufgabe |

These records are stored in the local SQLite database and are not included in the Git repository.

## ✅ Verification

The application was verified using Django's system checks, database migrations, and Django ORM queries.

The following relationships were successfully tested:

- Student to Student ID Card
- Student to Course
- Course to Professor
- Course to Semester
- Course to Course Description

## 🎯 Learning Objectives

This project demonstrates how to:

- Create Django models and database fields.
- Implement relational database relationships.
- Use `OneToOneField`, `ForeignKey`, and `ManyToManyField`.
- Generate and apply database migrations.
- Register models in Django Admin.
- Create and manage test records.
- Query related objects using the Django ORM.

## 📌 Project Status

**Completed:** All six database models have been implemented, migrated, and verified using sample data.

---

**Developed as part of a Django relational database modeling assignment.**