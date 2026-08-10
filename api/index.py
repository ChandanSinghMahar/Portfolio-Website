from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="../templates")

PROJECTS = [
    {
        "title": "Spam filtration",
        "Languages": "Python",
        "Description": "Check which email is spam or ham",
    },
    {
        "title": "Project 2",
        "Languages": "JAVA",
        "Description": "Mini game for fun",
    },
    {
        "title": "Project 3",
        "Languages": "HTML, CSS",
        "Description": "Web Portfolio",
    },
]


@app.route("/")
def hello_world():
    return render_template(
        "home.html",
        projects=PROJECTS,
        author_name="Chandan Singh Mahar"
    )


@app.route("/api/projects")
def list_project():
    return jsonify(PROJECTS)