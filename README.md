##Ticket Booking System (Flask + SQLite)
A full-stack Ticket Booking System web application that allows users to book Bus, Train, or Flight tickets via a clean, responsive, and interactive interface. 
The system dynamically calculates fare, stores booking details in SQLite, and displays a detailed booking history with a printable ticket format.

##Tech Stack
Layer	Technology
Frontend	: HTML, Bootstrap (CDN), JavaScript (Inline)
Backend   : Python (Flask)
Database	: SQLite (tickets.db)
Hosting	  : Render.com (Gunicorn)

##Features
Home Page to choose travel type (Bus, Train, Flight)
Booking Form to enter user and travel details
Auto Fare Calculation based on passenger count
Ticket Summary Page with all entered details
Booking History Page showing all past tickets in tabular format
Printable Ticket View
Responsive Design with Bootstrap 5


##Project Structure
ticket_booking_system/
├── static/
├── templates/
│   ├── home.html
│   ├── ticket.html
│   ├── bill.html
│   └── history.html
├── tickets.db
├── app.py
├── requirements.txt
├── Procfile
└── README.md

<img width="1920" height="974" alt="Screenshot (228)" src="https://github.com/user-attachments/assets/02faaca0-2c2f-46da-9847-85ea18386f25" />

