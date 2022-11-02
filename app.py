from flask import Flask, flash, request, render_template, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from datetime import date

from config import SECRET_KEY

from database.users import add_user, email_available, get_user_with_credentials, get_user_by_id
from database.tracker import add_entry, entry_exists, get_averages

import random

from mock_activity_api import mock_data

from quotes_api import data, raw_api

from pprint import pprint

# from scrapbook import allowed_file, upload_file

app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.login_message = 'Please log in to view this page.'
login_manager.login_message_category = 'error'


class User(UserMixin):

    def __init__(self, user_details):
        self.id = user_details.get('id')  # This one is important - it needs to be called self.id
        self.name = user_details.get('name')
        self.email = user_details.get('email')
        self.region = user_details.get('region')


@login_manager.user_loader
def user_loader(user_id):
    user_details = get_user_by_id(user_id)
    if user_details is None:
        return None
    user = User(user_details)
    return user


@app.get('/')
def view_home():
    entry_exists_for_today = current_user.is_authenticated and entry_exists(current_user.id, date.today())
    return render_template("home.html", user=current_user, entry_exists_for_today=entry_exists_for_today)


@app.get('/login')
def view_login():
    if not current_user.is_anonymous:
        return redirect('/')
    return render_template("login.html")


@app.post('/login')
def submit_login():
    if not current_user.is_anonymous:
        return redirect('/')
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user_with_credentials(email, password)
    if user is None:
        flash("Invalid credentials.", 'error')
    else:
        user = User(user)
        login_user(user)
        return redirect('/')
    return redirect('/login')


@app.get('/signup')
def view_signup():
    if not current_user.is_anonymous:
        return redirect('/')
    return render_template("signup.html")


@app.post('/signup')
def submit_signup():
    if not current_user.is_anonymous:
        return redirect('/')
    name = request.form.get('name')
    email = request.form.get('email')
    region = request.form.get('region')
    password = request.form.get('password')
    if len(password) < 8:
        flash("Passwords should be at least 8 characters long.", 'error')
    elif not email_available(email):
        flash("An account with that email already exists.", 'error')
    else:
        add_user(name, email, region, password)
        flash("New account created.", 'info')
        return redirect('/login')
    return redirect('/signup')


@app.post('/logout')
@login_required
def submit_logout():
    logout_user()
    return redirect('/')


@app.get("/today")
@login_required
def view_tracker():
    return render_template("daily-tracker.html", user=current_user)


@app.post("/today")
@login_required
def submit_tracker():  # can we create a class similar to this for the  - use this as the parent class
    mood = request.form.get("mood")
    sleep = request.form.get("sleep")
    motivation = request.form.get("motivation")
    reflection = request.form.get("reflection")
    if mood and sleep and motivation and reflection:
        add_entry(current_user.id, date.today(), mood, sleep, motivation, reflection)
        return redirect('/thanks')
    else:
        flash("Please don't leave fields blank.")
        return redirect('/today')


@app.get('/thanks')
@login_required
def view_tracker_thanks():
    return render_template("thanks.html", user=current_user)


@app.get('/month')
@login_required
def view_monthly_tracker():
    averages = get_averages(current_user.id)
    print(averages)
    return 5


# @app.route("/scrapbook")
# @login_required
# def scrapbook():
#     return render_template("scrapbook.html", user=current_user)
#
#
# @app.post("/scrapbook_entry")
# @login_required
# def submit_scrapbook():
#     image_url = request.form.get("image_url")
#     for filename, file in request.files:
#         # name = request.FILES[filename].name
#         print(filename, file)
#     # valid_image = allowed_file(image_url)
#     # upload_file(valid_image)


@app.get('/activity')
@login_required
def generate_activity():
    index = random.randint(0, len(mock_data) - 1)
    value = mock_data[index]
    return render_template("activity.html", data=value)


@app.get('/quote')
@login_required
def get_quote():
    integer = random.randint(0, 33)
    quote_obj = data[integer]
    return render_template("quotes.html", id=quote_obj["id"], author=quote_obj["person"], quote=quote_obj["quote"])


if __name__ == '__main__':
    app.run()
