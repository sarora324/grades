from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('homepage.html')

@app.route('/', methods=['POST'])
def my_form_post():
    number_assignment = request.form['number_assign']
    return number_assignment
