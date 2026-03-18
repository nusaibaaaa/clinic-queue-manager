from flask import Flask, render_template, request, redirect
from models import Patient
from queue_manager import add_patient, next_patient, get_queue, total_seen

app = Flask(__name__)


@app.route("/")
def home():

    patients = get_queue()

    return render_template("index.html", patients=patients)


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        symptoms = request.form["symptoms"]

        patient = Patient(name, age, symptoms)

        add_patient(patient)

        return redirect("/")

    return render_template("register.html")


@app.route("/next")
def call_next():

    next_patient()

    return redirect("/")


@app.route("/stats")
def stats():

    total = total_seen()

    return render_template("stats.html", total=total)


if __name__ == "__main__":
    app.run(debug=True)