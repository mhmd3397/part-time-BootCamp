from django.shortcuts import render, redirect
import random
from datetime import datetime


def initialize_game(request):
    request.session['gold'] = 0
    request.session['activities'] = []


def process_activity(request, activity):
    activity['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request.session['gold'] += activity['gold']
    request.session['activities'].append(activity)
    request.session.save()


# @app.route('/')
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    activities = {
        'activities': reversed(request.session['activities'])
    }
    return render(request, 'index.html', activities)


# @app.route('/process_money', methods=['POST'])
def process_money(request):
    building = request.POST['building']
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
    process_activity(request, activity)
    return redirect('/')


# @app.route('/reset')
def reset(request):
    initialize_game(request)
    return redirect('/')
