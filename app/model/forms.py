from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class FormPessoa(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    min = 12
    idade = IntegerField('idade',
                         validators=[NumberRange(min=min, message="Não deve ser menor que {} anos!".format(min))])
    submit = SubmitField('cadastrar')
