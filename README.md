# MyNotes web app

This is a web application that allows users to register, log in, and manage their personal notes. Users can add, view, and remove notes.


### Video Demo: https://youtu.be/Wl091UzYmCE


### Description:

A Flask app that allows user to store Notes online. It provides user the option to add and delete notes. Initially user is greeted with a login page. Login credentials are stored in SQL database. For unregistered user there is an option to register themselves given at the login page itself. After successfully logging in user is taken to home page where all user notes are displayed as nicely formatted cards. Also user is provided with menu of options namely "Home", "AddNote", "RemoveNote" upon clicking which user is taken to the respective pages.

* #### Features
    * User registration and login
    * Password hashing for security
    * Session management
    * Add, view, and remove notes

* #### Technologies Used
    * Python
    * Flask
    * SQLite
    * CS50 Library
    * Werkzeug for password hashing

* #### Usage
    * execute with "flask run"
    * Register a new user account.
    * Log in with your credentials.
    * Add, view, and remove notes.

* #### Required Libraries:
    * cs50
    * Flask
    * Flask-Session
    * requests

* #### File Structure
    * app.py: Main application file.
    * templates/: HTML templates for rendering web pages.
    * helpers.py: Helper functions for managing notes and user sessions.

### Detailed description of project Structure and Code
Root directory is named "project" and it contains the following files and folders:

* #### Folders
    * savedfiles
    * static
    * templates

* #### Files
    * app.py
    * helpers.py
    * README.md
    * requirements.txt
    * users.db

Description of the above mentioned is as follows:

* #### savedfiles:
    Notes created by user are saved here. Saved files are created using "user_id" as name of save_file which is unique for every user.

* #### static:
    Contains images and the CSS file for styling the pages.

* #### templates:
    * Contains the HTML templates used in the project where "layout.html" is the main template and all other templates extends it:

        * ##### addnote.html
            Contains two input fields 'title' and 'detail' and a button 'addnote' which submits the details entered by user to the route "/addnote".

        * ##### index.html
            Loops through the user's note's dictionary and dynamically generate and displays the information formatted as cards.

        * ##### layout.html
            Parent template that contains the basic structure of all the webpages. Bootstraps the webpages and also includes meta tag to make webpages look good on small screen devices like mobile phone.

        * ##### login.html
            Hosts two input field namely 'username' and 'password' and a submit button named 'login'.

        * ##### register.html
            Ask user to input 'username' and 'password'. Also mandates re-entering password to ensure correctness.

        * ##### removenote.html
            Dynamically generates a dropdown list of user's notes. Thus provides functionality to select and delete notes.

* #### app.py
    * Main application file that contains the following function and routes:

        * #### after_request
            * * Ensure responses aren't cached.
            * Executed after each request to the web application.

        * ##### "/register"
            * Renders register page.
            * Ensure validity of username and password.
            * Hashes the password using 'Werkzeug'.
            * Stores the user login credentials in SQL database 'users.db'.
            * Use placeholders in SQL queries to avoid injection attack.
            * Provide relevant feedback to user using 'flash'.

        * ##### "/login"
            * Renders login page.
            * Ensure validity of username and password.
            * Use placeholders in SQL queries to avoid injection attack.
            * Provide relevant feedback to user using 'flash'.

        * ##### "/"
            * Renders home page.
            * Access users notes using helper function.
            * Displays user notes formatted as rectangular cards.

        * ##### "/addnote"
            * Renders addnote page.
            * Lets user enter the 'title' and 'details' of note.
            * Adds the information to notes collection and save to file.

        * ##### "/removenote"
            * Renders removenote page.
            * Lets user select the 'title' of note from a dropdown list.
            * Deletes the note from collection and save the file.

        * ##### "/logout"
            * Logs user out

* #### helpers.py
    * Contains the following helper functions:

        * ##### login_required
            Ensures that a valid user is logged in.

        * ##### open_user_notes
            Fetches the notes of current logged in user. In case no saved file exist for the current user then creates a new file.

        * ##### save_notes
            Saves the notes of the user in a binary file using pickle module. And uses
            "user_id" from user database as file name to ensure uniqueness of file.



* #### README.md
    Detailed description of project.

* #### requirements.txt
    List of pip installable libraries.

* #### users.db
    SQL database. Contains table to store users login credentials i.e. username and hashed-password. Table is Indexed for faster access.

### Acknowledgment:

* #### CS50 Duck
    The duck has been a GREAT help! Saved a lot of time by helping in finding required libraries and helping with syntax usage, thus I could invest my time to focus more on core logic.
