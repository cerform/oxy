from flask import Flask, render_template, request, redirect
from utils.google_sheets import add_entry_to_sheets
from datetime import datetime

app = Flask(__name__)

# Департаменты и лаборатории
DEPARTMENTS = {
    "Biochemistry": ["Genetics Lab", "Protein Research Lab"],
    "Physics": ["Quantum Mechanics Lab", "Optics Lab"],
    "Chemistry": ["Organic Chemistry Lab", "Analytical Chemistry Lab"],
    "Engineering": ["Robotics Lab", "Nanotechnology Lab"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = request.form["name"]
        worker_id = request.form["worker_id"]
        floor = request.form["floor"]
        department = request.form["department"]
        lab = request.form["lab"]
        liters = request.form["liters"]

        add_entry_to_sheets([timestamp, name, worker_id, floor, department, lab, liters])

        return redirect("/")

    return render_template("index.html", departments=list(DEPARTMENTS.keys()), labs=DEPARTMENTS)

if __name__ == "__main__":
    app.run(debug=True)
