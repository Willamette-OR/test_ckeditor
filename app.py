from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor, CKEditorField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'foobar'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ckeditor = CKEditor(app)


# create the database and needed models
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Text)

db.create_all()


# create needed forms
class NoteForm(FlaskForm):
    note = CKEditorField('Notes', 
                         validators=[DataRequired(), Length(min=0, max=200)])
    submit = SubmitField('Submit')


# view functions
@app.route('/', methods=['GET', 'POST'])
def index():
    note = Note.query.get(1)
    form = NoteForm()
    if form.validate_on_submit():
        Note.query.delete()
        note = Note(note=form.note.data)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('notes.html', title='Notes', form=form, note=note)


if __name__ == '__main__':
    app.run()
