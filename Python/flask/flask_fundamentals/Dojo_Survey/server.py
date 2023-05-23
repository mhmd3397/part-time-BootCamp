'''
This module is for assignment Dojo Survey in Coding Dojo
Mohammed Eleyan
22-05-2023
'''

from flask import Flask, render_template, request  # added request
app = Flask(__name__)
# our index route will handle rendering our form


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/results', methods=['POST'])
def create_user():
    print("Got result Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    textarea_from_form = request.form['textarea']
    return render_template("results.html", name_on_template=name_from_form,
                           location_on_template=location_from_form,
                           language_on_template=language_from_form,
                           textarea_on_templates=textarea_from_form)


if __name__ == "__main__":
    app.run(debug=True)
