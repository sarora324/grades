from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms.fields import IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class EntryCategories(FlaskForm):
    category = SelectField('category', choices=[('Exams','Exams'),('Quizzes','Quizzes'),('HW','HW'),('Projects','Projects')])
    percentage = IntegerField('percentage', validators=[DataRequired(), NumberRange(min=0, max=100)])
    numberItems = IntegerField('numberitems', validators=[DataRequired(), NumberRange(min=0, max=50)])
=======
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    submit = SubmitField('Calculate')
>>>>>>> 7d8d0e2952a8ccf85c023e03fdb11f950582e364
