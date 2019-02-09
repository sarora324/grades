from flask import Flask, request, render_template
from form import RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfjsd824923'

@app.route('/')
def my_form():
    form = RegistrationForm()
    return render_template('homepage.html', title="Register", form=form)
