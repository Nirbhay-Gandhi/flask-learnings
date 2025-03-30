from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from forms import UserRegistrationForm, UserLoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4b3c1f2d4e5a6b7c8d9e0f1g2h3i4j5k6l7m8n9o0p'  # Secret key for CSRF protection

posts = [
    {
        "author": "John Doe",
        "title": "Blog Post 1",
        "content": "This is the first blog post content.",
        "date_posted": "2023-10-01"
    },
    
    {
        "author": "Karan Singh",
        "title": "Blog Post 2",
        "content": "This is the second blog post content.",
        "date_posted": "2024-12-14"
    }
]



"""
forward '/' is the root of the website, this is the first page that will be displayed when you visit the website
"""
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", posts=posts)  #passing variables into the template
#whatever variable we pass as an argument in the render_template function, we can access it in the template using the same name

@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register_func():
    form = UserRegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login_func():
    form = UserLoginForm()
    return render_template("login.html", title="Login", form=form)





if __name__ == "__main__":
    app.run(debug=True)

"""
<!--
- Code Block in Jinja
{% %}

- printing a variable in Jinja
{{ variable_name }}

- template inheritance in Jinja
-->
"""