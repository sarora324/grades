from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('homepage.html')

@app.route('/hello')
def hello():
    return 'Hello, World'
