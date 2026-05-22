# 📝 To-Do Manager (Python)

A simple yet structured **Command Line To-Do Manager Application** built using Python.

This project helps users **manage daily tasks efficiently** by allowing them to add, view, update, delete, and mark tasks as completed. It is designed to improve understanding of **Python fundamentals, project structure, functions, file handling, and exception handling**.

---

## 🚀 Features

### Core Features
- ➕ Add new tasks
- 📋 View all tasks
- ❌ Delete tasks
- ✅ Mark tasks as completed
- 🔄 Update existing tasks
- 🔍 Search tasks

### Advanced Features
- ⚠️ Task priority system (High / Medium / Low)
- 📅 Due date management
- 💾 Permanent storage using file handling
- 🔁 Auto-load saved tasks
- 📊 Task statistics

---

## 🛠️ Concepts Practiced

This project covers important Python concepts such as:

- Variables & Data Types
- Lists & Dictionaries
- Loops (`for`, `while`)
- Conditional Statements (`if-else`)
- Functions
- Exception Handling (`try-except`)
- File Handling
- JSON Handling
- Menu Driven Programs
- Project Structure

---

## 📂 Project Structure

```text
todo-manager/
│
├── main.py
├── task_manager.py
├── storage.py
├── tasks.json
├── README.md
└── assets/
```

### File Explanation

| File | Purpose |
|------|----------|
| `main.py` | Runs the application |
| `task_manager.py` | Contains task-related logic |
| `storage.py` | Handles saving/loading tasks |
| `tasks.json` | Stores tasks permanently |
| `README.md` | Project documentation |

---

## 📌 Task Structure Example

Each task is stored using a dictionary format:

```python
{
    "task": "Study Operating System",
    "status": "Pending",
    "priority": "High",
    "due_date": "25 May"
}
```

---

## 🎯 Learning Outcome

Through this project, I practiced:

- Writing clean and modular Python code
- Building menu-driven applications
- Managing data using lists and dictionaries
- Handling user input errors effectively
- Saving data permanently using file handling
- Structuring beginner-level projects professionally

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-link>
```

2. Navigate to project folder

```bash
cd todo-manager
```

3. Run the project

```bash
python main.py
```

---

## 📸 Project Preview

Example Menu:

```text
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Complete
5. Update Task
6. Search Task
7. Exit
```

---

## 🔮 Future Improvements

- GUI version using Tkinter
- Database integration
- Reminder system
- Login system
- Web version using Flask/Django

---

## 👨‍💻 Author

**Mahi Jindal**  
B.Tech CSE (AI/ML) | Python & AI/ML Learner

---

⭐ If you found this project useful, consider giving it a star.
