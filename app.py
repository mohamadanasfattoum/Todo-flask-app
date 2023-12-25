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





@app.get('/')
def home():
    todo_tist = db.session.query(Todo).all()
    return render_template('base.html', todo_list=todo_list)

@app.post('/add')
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=fals)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))




if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)