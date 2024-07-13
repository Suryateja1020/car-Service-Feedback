from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
import logging

app = Flask(__name__)

ENV = 'dev'  # Change to 'prod' in production

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgre%40123@localhost:5432/mirror_db'
else:
    app.debug = False
    # Set your production database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'your_production_database_uri_here'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

logging.basicConfig(level=logging.INFO)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        logging.info(f"Received feedback from {customer} about {dealer}")
        
        if customer == '' or dealer == '':
            logging.warning("Customer or dealer field is empty")
            return render_template('index.html', message='Please enter required fields')
        
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            logging.info("Feedback successfully submitted and email sent")
            return render_template('success.html')

        logging.warning("Feedback already submitted by this customer")
        return render_template('index.html', message='You have already submitted feedback')

if __name__ == '__main__':
    app.run(debug=True)
