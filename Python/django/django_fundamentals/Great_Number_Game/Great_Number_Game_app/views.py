from django.shortcuts import render, redirect
import random


def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['count'] = 0
        request.session['success'] = False
        request.session['result'] = ''

    print("Correct number:", int(request.session['number'])/3.3)

    used_in_templates = {
        'result': request.session['result'],
        'count': request.session['count'],
        'success': request.session['success']
    }
    return render(request, 'index.html', used_in_templates)


def guess(request):
    guess = int(request.POST['guess'])
    request.session['count'] += 1

    if guess < int(request.session['number']):
        request.session['result'] = 'Too low!'
    elif guess > request.session['number']:
        request.session['result'] = 'Too high!'
    else:
        request.session['result'] = 'Correct! You guessed the number.'
        request.session['success'] = True

    used_in_templates = {
        'result': request.session['result'],
        'count': request.session['count'],
        'success': request.session['success']
    }
    return redirect('/', used_in_templates)


def play_again(request):
    request.session.pop('number')
    request.session.pop('count')
    request.session.pop('success')
    request.session.save()
    return redirect('/')
