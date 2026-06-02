from flask import Flask, render_template_string, request, redirect
from db import get_connection
app = Flask(__name__)
@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>To-Do List</title>
    </head>
    <body style="text-align:center">
        <h1>To-Do List Application</h1>

        <form action="/add" method="POST">
            <input type="text" name="task" placeholder="Enter Task" required>
            <button type="submit">Add Task</button>
        </form>

        <hr>

        {% for task in tasks %}
        <p>
            <strong>{{ task[1] }}</strong>
            - {{ task[2] }}

            <a href="/complete/{{ task[0] }}">Complete</a>

            <a href="/delete/{{ task[0] }}">Delete</a>
        </p>
        {% endfor %}

    </body>
    </html>
    """
    return render_template_string(html, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (t_name) VALUES (%s)",
        (task,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status='Completed' WHERE task_id=%s",
        (task_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE task_id=%s",
        (task_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)