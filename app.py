from flask import Flask, flash, request, render_template, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.utils import secure_filename
import requests
from datetime import date
from random import randint
from os import mkdir, remove
from os.path import join, dirname, realpath, exists

from config import SECRET_KEY

from database.users import add_user, email_available, get_user_with_credentials, get_user_by_id
from database.tracker import add_or_update_entry, get_entry, get_averages
from database.scrapbook import add_image, get_images, remove_image

from utils.files import get_file_extension, is_valid_image_file

from api.mock_activity_api import create_activity_api
from api.quotes_api import QuoteGenerator
from api.photos_api import PhotoGenerator

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'static/uploads')
app.config['PORT'] = 5000

if not exists(app.config['UPLOAD_FOLDER']):
    mkdir(app.config['UPLOAD_FOLDER'])

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.login_message = 'Please log in to view this page.'
login_manager.login_message_category = 'error'

activity_api = create_activity_api()
quote_generator = QuoteGenerator()
photo_generator = PhotoGenerator()


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
    quote = quote_generator.get_random_quote()
    return render_template("home.html", user=current_user, quote=quote)


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
    existing_entry = get_entry(current_user.id, date.today())
    existing_mood = existing_entry['mood'] if existing_entry else 0
    existing_sleep = existing_entry['sleep'] if existing_entry else 0
    existing_motivation = existing_entry['motivation'] if existing_entry else 0
    existing_reflection = existing_entry['reflection'] if existing_entry else ''
    return render_template("daily-tracker.html", user=current_user, existing_mood=existing_mood,
                           existing_sleep=existing_sleep, existing_motivation=existing_motivation, existing_reflection=existing_reflection)


@app.post("/today")
@login_required
def submit_tracker():
    mood = request.form.get("mood")
    sleep = request.form.get("sleep")
    motivation = request.form.get("motivation")
    reflection = request.form.get("reflection")
    if mood and sleep and motivation and reflection:
        add_or_update_entry(current_user.id, date.today(), mood, sleep, motivation, reflection)
        return redirect('/thanks')
    else:
        flash("Please don't leave fields blank.", 'error')
        return redirect('/today')


@app.get('/thanks')
@login_required
def view_tracker_thanks():
    return render_template("thanks.html", user=current_user)


@app.get('/month')
@login_required
def view_monthly_tracker():
    averages = get_averages(current_user.id)
    average_mood = averages['average_mood']
    average_sleep = averages['average_sleep']
    average_motivation = averages['average_motivation']
    return render_template("monthly-averages.html", average_mood=average_mood, average_sleep=average_sleep, average_motivation=average_motivation)


@app.get('/activity')
@login_required
def view_activity():
    response = requests.get(f"http://localhost:{app.config['PORT']}/activity-api")
    data = response.json()
    activity = data['activity']
    photo = photo_generator.get_random_picture()
    print(photo)
    return render_template("activity.html", activity=activity, photo=photo)


@app.get("/scrapbook")
@login_required
def view_scrapbook():
    images = get_images(current_user.id)
    return render_template("scrapbook.html", user=current_user, images=images)


@app.get("/scrapbook/upload")
@login_required
def view_scrapbook_upload():
    return render_template("scrapbook-upload.html", user=current_user)


@app.post("/scrapbook/upload")
@login_required
def submit_scrapbook_upload():
    file = request.files.get('file')
    if not file or not file.filename:
        flash('Please select a file', 'error')
    elif not is_valid_image_file(file.filename):
        flash('Please only select .png, .jpg, .jpeg or .gif files', 'error')
    else:
        filename = f"{current_user.id}-{randint(10000000, 99999999)}.{get_file_extension(file.filename)}"
        file.save(join(app.config['UPLOAD_FOLDER'], filename))
        add_image(current_user.id, filename)
        flash('Your file has been uploaded', 'info')
        return redirect('/scrapbook')
    return redirect('/scrapbook/upload')


@app.post("/scrapbook/delete/<image_url>")
@login_required
def submit_scrapbook_deletion(image_url):
    if image_url.split('-')[0] == str(current_user.id):  # If the image belongs to the current user
        try:
            remove(join(app.config['UPLOAD_FOLDER'], secure_filename(image_url)))
        except FileNotFoundError:
            pass
        else:
            remove_image(current_user.id, image_url)
    return redirect('/scrapbook')


if __name__ == '__main__':
    combined_app = Flask(__name__)
    combined_app.wsgi_app = DispatcherMiddleware(app, {
        '/activity-api': activity_api
    })
    combined_app.run(port=app.config['PORT'])
