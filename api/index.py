from flask import Flask, render_template, jsonify
from database.database import load_projects_from_db

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/")
def hello_chandan():
    projects = load_projects_from_db()
    return render_template(
        "home.html",
        projects=projects,
        author_name="Chandan Singh Mahar"
    )


@app.route("/api/projects")
def list_project():
    return jsonify(PROJECTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

