# Import Flask to allow us to create our app
from flask import Flask, render_template

app = Flask(__name__)  # Create a new instance of the Flask class called "app"


@app.route('/')
def hello_world():
    # Instead of returning a string,
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')

# import statements, maybe some other routes


@app.route('/success')
def success():
    return "success"

# app.run(debug=True) should be the very last statement!


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name


# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
