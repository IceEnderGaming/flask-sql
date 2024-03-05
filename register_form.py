from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect, render_template, Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


class LoginForm(FlaskForm):
    login = StringField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/register', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.submit.data)
    if form.submit.data:
        add_user(form)
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)


def add_user(form):
    user = User()
    user.email = form.login.data
    user.surname = form.surname.data
    user.name = form.name.data
    user.age = form.age.data
    user.position = form.position.data
    user.speciality = form.speciality.data
    user.address = form.address.data
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html', title='Успешно')


app.run(debug=True, host="127.0.0.1", port=5000)
