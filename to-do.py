from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory task list
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    priority = request.form.get('priority', 'low')  # default is 'low'
    
    if task_text:
        todo_list.append({
            'task': task_text,
            'done': False,
            'priority': priority.lower(),
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return redirect(url_for('index'))

@app.route('/done/<int:index>')
def done(index):
    if 0 <= index < len(todo_list):
        todo_list[index]['done'] = not todo_list[index]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todo_list):
        del todo_list[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
