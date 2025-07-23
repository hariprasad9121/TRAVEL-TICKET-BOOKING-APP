from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Create database
def init_db():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    mobile TEXT,
                    age INTEGER,
                    ticket_type TEXT,
                    source TEXT,
                    destination TEXT,
                    date TEXT,
                    no_of_tickets INTEGER,
                    price_per_ticket INTEGER,
                    grand_total INTEGER
                )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book/<ticket_type>')
def book(ticket_type):
    prices = {'Bus': 500, 'Train': 250, 'Flight': 2000}
    price = prices.get(ticket_type, 0)
    return render_template('ticket.html', ticket_type=ticket_type, price=price)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    name = data['name']
    email = data['email']
    mobile = data['mobile']
    age = int(data['age'])
    source = data['source']
    destination = data['destination']
    travel_date = data['travel_date']
    no_of_tickets = int(data['no_of_tickets'])
    ticket_type = data['ticket_type']
    price_per_ticket = int(data['price'])
    grand_total = price_per_ticket * no_of_tickets

    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute('''INSERT INTO bookings 
                 (name, email, mobile, age, ticket_type, source, destination, date, no_of_tickets, price_per_ticket, grand_total)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (name, email, mobile, age, ticket_type, source, destination, travel_date, no_of_tickets, price_per_ticket, grand_total))
    conn.commit()
    conn.close()

    session['ticket'] = dict(data)
    session['ticket']['grand_total'] = grand_total
    return redirect(url_for('bill'))

@app.route('/bill')
def bill():
    ticket = session.get('ticket', None)
    if not ticket:
        return redirect(url_for('home'))
    return render_template('bill.html', ticket=ticket)

@app.route('/history')
def history():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT name, ticket_type, source, destination, date, no_of_tickets, grand_total FROM bookings")
    bookings = c.fetchall()
    conn.close()
    return render_template('history.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
