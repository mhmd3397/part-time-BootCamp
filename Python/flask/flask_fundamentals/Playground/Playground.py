'''
This module is for assignment Understanding Routing in Coding Dojo
Mohammed Eleyan
20-05-2023
'''


# Internal Styling
# Just for this assignment, use an internal stylesheet or inline CSS (review here).


from flask import Flask, render_template
app = Flask(__name__)


# Level 1
# When a user visits http://localhost:5000/play,
# # have it render three beautiful looking blue boxes.
# # Please use a template to render this.


@app.route('/play')
def index2(times=int(3), color="#9fc5f8"):
    return render_template("index.html", times=int(times), color=color)


# Level 2
# When a user visits localhost:5000/play/(x),
# # have it display the beautiful looking blue boxes x times.
# # For example, localhost:5000/play/7 should display these blue boxes 7 times.
# # Calling localhost:5000/play/35 would display these blue boxes 35 times.
# # Please remember that x originally is a string, and if you want to use it as an integer,
# # you must first convert it to integer using int(). For example int("7") returns 7.


@app.route('/play/<times>')
def index3(times):
    return render_template("index.html", times=int(times), color="#9fc5f8")


# Level 3
# When a user visits localhost:5000/play/(x)/(color),
# # have it display beautiful looking boxes x times,
# # but this time where the boxes appear in (color).
# # For example, localhost:5000/play/5/green would display 5 beautiful green boxes.
# # Calling localhost:5000/play/35/red would display 35 beautiful red boxes.


@app.route('/play/<times>/<color>')
def index4(times, color):
    return render_template("index.html", times=int(times), color=color)


if __name__ == "__main__":
    app.run(debug=True)
