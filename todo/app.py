from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        tasks.append(task_content)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        new_task_content = request.form.get('updated_task')
        if new_task_content:
            tasks[task_id] = new_task_content
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)