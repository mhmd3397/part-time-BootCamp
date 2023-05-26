'''
This module is for assignment Ninja Gold in Coding Dojo
Mohammed Eleyan
26-05-2023
'''


from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


def initialize_game():
    session['gold'] = 0
    session['activities'] = []


def process_activity(activity):
    activity['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session['gold'] += activity['gold']
    session['activities'].append(activity)


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html',
                           activities=reversed(session['activities']))


@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building == 'farm':
        gold = random.randint(10, 20)
        activity = {
            'message': f"Earned {gold} gold from the farm!",
            'gold': gold
        }
    elif building == 'cave':
        gold = random.randint(5, 10)
        activity = {
            'message': f"Earned {gold} gold from the cave!",
            'gold': gold
        }
    elif building == 'house':
        gold = random.randint(2, 5)
        activity = {
            'message': f"Earned {gold} gold from the house!",
            'gold': gold
        }
    elif building == 'casino':
        gold = random.randint(-50, 50)
        if gold < 0:
            activity = {
                'message': f"Entered a casino and lost {abs(gold)}"
                f" gold... Ouch!",
                'gold': gold
            }
        else:
            activity = {
                'message': f"Entered a casino and won {gold} gold!",
                'gold': gold
            }

    process_activity(activity)
    return redirect('/')


@app.route('/reset')
def reset():
    initialize_game()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
