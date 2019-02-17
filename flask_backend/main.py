from flask import Flask, request, render_template, url_for, flash, redirect
from form import EntryCategories
app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfjsd824923'

#@app.route('/', methods=['GET', 'POST'])
@app.route('/')
def homepage():
    return render_template('index.html', token="Hello Flask+React")
    #myEntry = EntryCategories()
    #if myEntry.validate_on_submit():
        #flash(f'Account created for you', 'success')
    #print(request.args.get('num_forms'))
    #return render_template('homepage.html', title="Entry", form=myEntry)
