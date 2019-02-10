from flask import Flask, request, render_template
from form import EntryCategories
app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfjsd824923'

@app.route('/')
def homepage():
    myEntry = EntryCategories()
    print(request.args.get('num_forms'))
    return render_template('homepage.html', title="Entry", form=myEntry)
