import pickle


from flask import redirect, session
from functools import wraps


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def open_user_notes(user_id):
    """Load user notes from saved file OR Create new file if none exist"""

    try:
        with open(f"savedfiles/{user_id}.pkl", "rb") as file:
            notes_dictionary = pickle.load(file)
    except FileNotFoundError:
        notes_dictionary = {}
        save_notes(user_id, notes_dictionary)

    return notes_dictionary


def save_notes(user_id, notes_dictionary):
    """Save notes in binary file"""

    with open(f"savedfiles/{user_id}.pkl", "wb") as file:
        pickle.dump(notes_dictionary, file)
