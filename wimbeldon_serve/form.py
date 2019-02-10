from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class EntryCategories(FlaskForm):
    category = SelectField('category', choices=[('Exams','Exams'),('Quizzes','Quizzes'),('HW','HW'),('Projects','Projects')])
    percentage = IntegerField('percentage', validators=[DataRequired(), NumberRange(min=0, max=100)])
    numberItems = IntegerField('numberitems', validators=[DataRequired(), NumberRange(min=0, max=50)])
