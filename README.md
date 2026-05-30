# Event Registration System

## Project Overview
The Event Registration System is a web-based application developed using Python, Flask, and SQLite. It allows users to create events and register participants for those events. The project demonstrates basic backend development concepts such as routing, database management, form handling, and user interaction.

## Features
- Add new events
- View available events
- Register users for events
- Store event and registration data in SQLite database
- Display registered participants

## Technologies Used
- Python
- Flask
- SQLite
- HTML

## Project Structure

```text
CodeAlpha_EventSystem/
│
├── app.py
├── database.db
├── requirements.txt
├── templates/
│   ├── index.html
│   └── register.html
└── static/
```

## Installation

1. Clone the repository:

```bash
git clone <repository-link>
```

2. Navigate to the project directory:

```bash
cd CodeAlpha_EventSystem
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Usage

### Add Event
- Enter event title, date, and location.
- Click "Add Event".

### Register for Event
- Select an available event.
- Enter participant details.
- Submit the registration form.

### View Registrations
Visit:

```text
http://127.0.0.1:5000/registrations
```

to view all registered participants.

## Learning Outcomes
Through this project, I learned:
- Flask application development
- Database integration using SQLite
- CRUD operations
- Routing and templates in Flask
- Form handling and data storage

## Internship Project
This project was developed as part of the Backend Development Internship at CodeAlpha.

## Author
Manasa
