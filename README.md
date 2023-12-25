# TODO_APP

The project "Todo-flask-app" is a GitHub repository created by mohamadanasfattoum. It is a Todo App built using the Flask web framework.

The main purpose of the Todo App is to provide a simple and user-friendly interface for managing tasks or to-do items. Users can create new tasks, mark them as complete, update task details, and delete tasks from the list. The application utilizes various technologies such as Python, Flask, HTML/CSS, JavaScript, Bootstrap, and Flask-SQLAlchemy.

To run the Todo App project, you can follow these steps:

1. Clone the repository: You can clone the repository by using the "Clone" button on the GitHub page or by running the following command in your terminal:
   ````
   git clone https://github.com/mohamadanasfattoum/Todo-flask-app.git
   ```

2. Set up a virtual environment (optional): It is recommended to create a virtual environment to isolate the project dependencies. Navigate to the project directory and run the following command to create a virtual environment:
   ````
   python3 -m venv venv
   ```

3. Activate the virtual environment: Activate the virtual environment by running the appropriate command based on your operating system:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies: Once the virtual environment is activated, you need to install the project dependencies. Navigate to the project directory and run the following command:
   ````
   pip install -r requirements.txt
   ```

5. Set up the database: The Todo App uses Flask-SQLAlchemy to interact with a database. You need to initialize and migrate the database. Run the following commands in the project directory:
   ````
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application: After setting up the database, you can start the Flask development server by running the following command:
   ````
   flask run
   ```

   This will start the server, and you should see output indicating that the application is running. By default, the application can be accessed at http://localhost:5000 in your web browser.

That's it! You should now be able to access and use the Todo App in your local environment. Feel free to explore the code and make any necessary modifications or improvements according to your requirements.
