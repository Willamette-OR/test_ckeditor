from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'foobar'


class NoteForm(FlaskForm):
    note = TextAreaField('Notes', 
                         validators=[DataRequired(), Length(min=0, max=200)])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NoteForm()
    return render_template('notes.html', title='Notes', form=form)


if __name__ == '__main__':
    app.run()
