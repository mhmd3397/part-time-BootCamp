'''
This module is for assignment checkerboard in Coding Dojo
Mohammed Eleyan
21-05-2023
'''


# Your program should have the following output.


from flask import Flask, render_template
app = Flask(__name__)


# http://localhost:5000 - should display 8 by 8 checkerboard


@app.route('/')
def index1(x=int(8), y=int(8)):
    return render_template("index.html", x=int(x), y=int(y))


# http://localhost:5000/4 - should display 8 by 4 checkerboard


@app.route('/<y>')
def index2(y,x=int(8)):
    return render_template("index.html", x=int(x), y=int(y))


# http://localhost:5000/(x)/(y) - should display x by y checkerboard.
#  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.
#  Before you pass x or y to Jinja,
#  please remember to convert it to integer first (so that you can use x or y in a for loop)


@app.route('/<x>/<y>')
def index3(x, y):
    return render_template("index.html", x=int(x), y=int(y))


if __name__ == "__main__":
    app.run(debug=True)
