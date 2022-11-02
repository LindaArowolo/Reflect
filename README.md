REFLECT

Reflect with Reflect!

This website helps you track your overall wellbeing by tracking your daily mood, quality of sleep, motivation level, and prompting you with a question about your daily thoughts and habits. Reflect was created with our users in mind—to aid them on their journey with their mental and emotional wellbeing. Along with a tracker, we also have a scrapbook section, which provides our users with an outlet to get all their thoughts out, whether this be via typing or uploading voice notes, videos or photos.
Our reflect software allows our users to reflect on their state of being, how they are living and if it is in alignment with their life intentions. You will Reflect with REFLECT.


Installation Guide
You will need to run the mysql scripts from the schema.sql file located in the sql_scripts directory.
Update the information on database.py in line with your own database credentials
Copy the contents from config.template.py into a new python folder called config.py. Here, you will need to generate your own API id and key https://www.back4app.com/database/back4app/list-of-largest-cities-in-uk and populate these into the corresponding fields
You will need to install the following python packages:
pip install flask
pip install mysql-connector-python
pip install requests
Once you have followed these steps, run the program from your python IDE. Click the link that appears in the terminal. This will display the login screen for the web app.

Navigation
Login Page
Select the 'Sign Up' hyperlink which will redirect you to the sign up page.
Sign Up Page
Enter your credentials here to register - username, email and password, and type your region from. Once you have successfully registered, it will display a success message, and will redirect you to the login page. Type in your credentials and hit 'log in'.
Dashboard
You will see a welcome message containing your name, then four options will appear. The four options that you can select are;

My day -  daily inputs into the journal.

My Month - ?

My Activities -  A suggestion of activities for you.
My Scrapbook - a space to upload your feelings or record your frame of mind through text, photos, videos and voice notes.

Log Out
Selecting log out returns you to the login screen.
