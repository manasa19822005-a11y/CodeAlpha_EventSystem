from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Event Table
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date = db.Column(db.String(50))
    location = db.Column(db.String(100))

# Registration Table
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    event_id = db.Column(db.Integer)

# Home Page
@app.route('/')
def home():
    events = Event.query.all()
    return render_template('index.html', events=events)

# Add Event
@app.route('/add-event', methods=['POST'])
def add_event():
    title = request.form['title']
    date = request.form['date']
    location = request.form['location']

    new_event = Event(title=title, date=date, location=location)

    db.session.add(new_event)
    db.session.commit()

    return redirect('/')

# Register Page
@app.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):

    if request.method == 'POST':
        username = request.form['username']

        registration = Registration(
            username=username,
            event_id=event_id
        )

        db.session.add(registration)
        db.session.commit()

        return "Registration Successful!"

    return render_template('register.html')

# View Registrations
@app.route('/registrations')
def registrations():
    all_registrations = Registration.query.all()

    output = ""

    for reg in all_registrations:
        output += f"User: {reg.username} registered for Event ID: {reg.event_id}<br>"

    return output

# Run Project
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)