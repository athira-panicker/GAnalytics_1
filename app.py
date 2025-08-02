from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    plan = request.form.get('plan')
    print(f"New signup: {name}, {email}, Plan: {plan}")
    return f"<h2>Thanks for signing up, {name}!</h2><p>You chose the {plan} plan.</p>"

if __name__ == '__main__':
    app.run(debug=True)
