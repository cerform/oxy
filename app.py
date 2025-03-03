import os
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
        print(request.form)  # Проверяем, какие данные приходят в консоль Render

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = request.form.get("name")
        worker_id = request.form.get("worker_id")
        floor = request.form.get("floor")
        department = request.form.get("department")
        lab = request.form.get("lab")
        liters = request.form.get("liters")

        if name and worker_id and floor and department and lab and liters:
            add_entry_to_sheets([timestamp, name, worker_id, floor, department, lab, liters])
            print("Record Was Succesfully added!")

        return redirect("/")

    return render_template("index.html", departments=list(DEPARTMENTS.keys()), labs=DEPARTMENTS)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Render передает PORT в окружении
    app.run(host="0.0.0.0", port=port)
