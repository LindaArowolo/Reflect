## **REFLECT**

### Reflect with Reflect.

This website helps you track your overall well-being by tracking your daily mood, quality of sleep, motivation level, and prompting you with a question about your daily thoughts and habits.
Reflect was created with our users in mind — to aid them on their journey with their mental and emotional wellbeing. Along with a tracker, we also have a scrapbook section, which provides our users with a space to document their memories by uploading photos.

Our Reflect software allows our users to reflect on their state of being, how they are living and if it is in alignment with their life intentions. You will Reflect with REFLECT.

### Installation Guide

You will need to run the mysql scripts from the schema.sql file located in the database directory.
Update the information within config.py in line with your own database credentials.
Copy the contents from config.template.py into a new python file called config.py. 

Please sign up to www.pexels.com and navigate to https://www.pexels.com/api/new/ to generate your own API key. Once you have your key, paste it into the PEXELS_API_KEY field in config.py - line 11 should look something like this:
`PEXELS_API_KEY = '{your-api-key}'`

You will need to install the following python packages:

- pip install Flask, 
- pip install Flask-Login, 
- pip install mysql-connector-python, 
- pip install requests, 
- pip install bcrypt,
- pip install Werkzeug,

Once you have followed these steps, run the program from your python IDE. Click the link that appears in the terminal. This will display the login screen for the web app.

### Navigation

#### Login Page

Select the 'Sign Up' hyperlink which will redirect you to the sign up page.

#### Sign Up Page

Enter your credentials here to register - username, email and password, and type your region from. Once you have successfully registered, it will display a success message, and will redirect you to the login page. Type in your credentials and hit 'log in'.

#### Dashboard

You will see a welcome message containing your name, then four options will appear. The four options that you can select are:

- My day - tracks your daily mood, sleep quality, motivation level and reflection for the day,
- My month - gives you a summary of your mood, sleep quality and motivation level entries for the last 30 days,
- My activities - generates a random relaxation activity for you to try,
- My scrapbook - a space to document your memories by uploading photos.

#### Log Out
Selecting log out returns you to the login screen.