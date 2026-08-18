from flask import Flask, render_template, jsonify, request
from database.database import load_projects_from_db, load_project_from_db, add_application_to_db

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
    )


@app.route("/api/projects")
def list_project():
    projects = load_projects_from_db()
    return jsonify(projects)

@app.route("/project/<int:id>")
def show_project(id):
    project =load_project_from_db(id)

    if not project:
        return "Not Found", 404
    return render_template("projectpage.html",project=project)

@app.route("/project/<int:id>/apply", methods=['post'])
def apply_to_project(id):
    data = request.form
    project = load_project_from_db(id)
    
    add_application_to_db(id, data)
    
    return render_template('application_submitted.html',
                            application=data,
                            project=project)

# remove it when in production
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)

