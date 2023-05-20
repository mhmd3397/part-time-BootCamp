'''
This module is for assignment Understanding Routing in Coding Dojo
Mohammed Eleyan
20-05-2023
'''
# Create a server file that generates the specified responses for the following url requests:

from flask import Flask

app = Flask(__name__)


# localhost:5000/ - have it say "Hello World!"


@app.route('/')
def hello_world():
    return 'Hello World!'

# localhost:5000/dojo - have it say "Dojo!"


@app.route('/dojo')
def dojo():
    return "Dojo!"

# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"


@app.route('/say/<name>')
def say(name):
    print(name)
    return f"Hi {name}!"

# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times


@app.route('/repeat/<num_of_repeats>/<name>')
def repeat(num_of_repeats, name):
    print(num_of_repeats)
    print(name)
    return f"{name} "*int(num_of_repeats)


if __name__ == "__main__":
    app.run(debug=True)
