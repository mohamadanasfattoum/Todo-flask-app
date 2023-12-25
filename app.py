from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Todo(db.Model): # database table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean())





@app.route('/')
def home():
    todo_list = db.session.query(Todo).all()
    return render_template('base.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update(todo_id):
    if request.method == 'POST':
        todo = Todo.query.get(todo_id)
        if todo is not None:
            todo.title = request.form.get("title")      
            db.session.commit()
        return redirect(url_for("home"))
    else:
        todo = Todo.query.get(todo_id)
        if todo is not None:
            return render_template("update.html", todo=todo)
        else:
            return redirect(url_for("home"))


@app.route('/delete/<int:todo_id>', methods=['GET'])
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    if todo is not None:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("home"))






if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)