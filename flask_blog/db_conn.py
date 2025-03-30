from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from forms import UserRegistrationForm, UserLoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4b3c1f2d4e5a6b7c8d9e0f1g2h3i4j5k6l7m8n9o0p'  # Secret key for CSRF protection


@app.route("/")
def home():
    return "<h1>hello<h1>"


if __name__ == "__main__":
    app.run(debug=True)
