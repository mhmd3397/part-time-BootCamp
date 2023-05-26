from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("index.html", counter=session["counter"])


@app.route('/counter', methods=['POST'])
def counter():
    if request.form["button"] == 'add':
        session["counter"] += 1
    elif request.form["button"] == 'reset':
        session["counter"] = 0
    return redirect('/')


@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
