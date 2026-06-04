# To-Do List Application

## Project Overview    

The To-Do List Application is a simple web-based task management system developed using Flask and MySQL. The application allows users to manage their daily tasks efficiently by providing functionalities such as adding new tasks, viewing existing tasks, marking tasks as completed, and deleting tasks.

This project demonstrates the fundamentals of web application development, including database connectivity, CRUD operations, routing, form handling, and user interaction through a web interface.   

---

# Technologies Used

* Python
* Flask
* MySQL
* HTML
* MySQL Connector for Python

---

# Project Features

### 1. Add Task

Users can create a new task by entering the task name in the input field and submitting the form.

### 2. View Tasks

All tasks stored in the database are displayed on the home page.

### 3. Complete Task

Users can mark a task as completed after finishing it.

### 4. Delete Task

Users can remove tasks that are no longer needed.

### 5. Persistent Storage

All task information is stored in a MySQL database, ensuring data remains available even after the application is restarted.

---

# Project Structure

```text
todo_app/
│
├── app.py
├── db.py
└── README.md
```

### app.py

Contains the Flask application logic, routes, and task management functionalities.

### db.py

Contains the database connection function used throughout the application.

### README.md

Provides project documentation and setup instructions.

---

# Database Design

## Database

```sql
CREATE DATABASE todo_db;
```

## Table

```sql
CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    t_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);
```

---

# Table Description

| Column Name | Data Type    | Description                               |
| ----------- | ------------ | ----------------------------------------- |
| task_id     | INT          | Unique identifier for each task           |
| t_name      | VARCHAR(100) | Stores the task name                      |
| status      | VARCHAR(20)  | Stores task status (Pending or Completed) |

### task_id

Automatically generates a unique ID for each task.

### t_name

Stores the task entered by the user.

### status

Tracks whether a task is pending or completed.

---

# Application Workflow

## Step 1: User Opens the Application

The application loads all tasks from the database and displays them on the home page.

### Result

Users can see all existing tasks along with their current status.

---

## Step 2: User Adds a New Task

The user enters a task name and submits it.

### Process

* The task is received by the Flask application.
* The task is inserted into the database.
* The status is automatically set to "Pending".
* The user is redirected back to the home page.

### Result

The newly added task appears in the task list.

---

## Step 3: User Completes a Task

The user selects a task and marks it as completed.

### Process

* The application updates the task status in the database.
* The task status changes from "Pending" to "Completed".

### Result

The updated status is displayed on the home page.

---

## Step 4: User Deletes a Task

The user selects a task and clicks the delete option.

### Process

* The application removes the task from the database.

### Result

The task disappears from the task list.

---

# CRUD Operations Implemented

CRUD stands for Create, Read, Update, and Delete.

| Operation | Description            |
| --------- | ---------------------- |
| Create    | Add a new task         |
| Read      | View all tasks         |
| Update    | Mark task as completed |
| Delete    | Remove a task          |

This project implements all four CRUD operations.

---

# Database Connection Process

The application establishes a connection to the MySQL database whenever a database operation is required.

### Connection Responsibilities

* Connect to the MySQL server
* Execute SQL queries
* Retrieve data
* Update records
* Delete records
* Save changes

After completing the operation, the connection is closed to free resources.

---

# Routing Overview

The application uses multiple routes to handle different operations.

| Route             | Purpose                  |
| ----------------- | ------------------------ |
| /                 | Display all tasks        |
| /add              | Add a new task           |
| /complete/task_id | Mark a task as completed |
| /delete/task_id   | Delete a task            |

---

# Installation Guide

## Step 1: Install Python

Verify Python installation:

```bash
python --version
```

---

## Step 2: Install Required Packages

```bash
pip install flask
pip install mysql-connector-python
```

---

## Step 3: Create Database

Open MySQL and execute:

```sql
CREATE DATABASE todo_db;

USE todo_db;

CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    t_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);
```

---

## Step 4: Configure Database Credentials

Update the database connection settings with your MySQL username and password.

---

## Step 5: Run the Application

```bash
python app.py
```

---

## Step 6: Open Browser

Visit:

```text
http://127.0.0.1:5000
```

---

# Learning Outcomes

Through this project, the following concepts can be learned:

* Flask Application Development
* Routing in Flask
* Form Handling
* MySQL Database Integration
* CRUD Operations
* Database Connectivity
* Web Application Workflow
* Task Management Systems

---

# Future Enhancements

The project can be enhanced by adding:

* User Authentication
* Task Editing
* Due Dates
* Task Categories
* Search Functionality
* Priority Levels
* Responsive User Interface
* REST API Support

---

# Conclusion

The To-Do List Application is a beginner-friendly Flask project that demonstrates how a web application interacts with a database to manage information. It provides hands-on experience with Flask routing, MySQL integration, CRUD operations, and web development fundamentals. The project serves as an excellent foundation for learning backend development and can be extended with additional features as development skills improve.
