from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['count'] = 0
        session['success'] = False
    return render_template('index.html', result='', count=session['count'],
                           success=session['success'])


@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    session['count'] += 1

    if guess < session['number']:
        result = 'Too low!'
    elif guess > session['number']:
        result = 'Too high!'
    else:
        result = 'Correct! You guessed the number.'
        session['success'] = True

    return redirect('/', result=result, count=session['count'],
                    success=session['success'])


@app.route('/play_again', methods=['POST'])
def play_again():
    session.pop('number')
    session.pop('count')
    session.pop('success')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
