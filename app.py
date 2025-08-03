from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("name")
    email = request.form.get("email")
    plan = request.form.get("plan")

    # Save data to signups.csv
    with open("signups.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, plan])

    print(f"New signup: {name}, {email}, Plan: {plan}")
    return f"<h2>Thanks for signing up, {name}!</h2><p>You chose the {plan} plan.</p>"

@app.route("/basic")
def basic():
    return render_template("basic.html")

@app.route("/freemium")
def freemium():
    return render_template("freemium.html")

@app.route("/premium")
def premium():
    return render_template("premium.html")

if __name__ == "__main__":
    app.run(debug=True)
