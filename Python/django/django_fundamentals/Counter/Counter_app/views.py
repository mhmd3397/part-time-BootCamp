from django.shortcuts import render, redirect


# @app.route('/')
def index(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    else:
        request.session["counter"] += 1
    return render(request, "index.html")


# @app.route('/counter', methods=['POST'])
def counter(request):
    if request.POST["button"] == 'add':
        request.session["counter"] += 1
    elif request.POST["button"] == 'reset':
        request.session["counter"] = 0
    elif request.POST["button"] == 'custom':
        if request.POST["increment"] == '':
            request.session["counter"] += -1
        else:
            request.session["counter"] += int(request.POST["increment"])-1
    return redirect('/')


# @app.route("/destroy_session")
def destroy(request):
    del request.session["counter"]
    return redirect("/")
