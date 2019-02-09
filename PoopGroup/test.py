from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello</h1>"
