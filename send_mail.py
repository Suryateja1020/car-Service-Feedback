
'''
import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = ''
    password = ''
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


        '''



'''
import smtplib

MY_EMAIL = "arrakis025@gmail.com"
MY_PASSWORD ="ppkk lils dndd qoqk"


with smtplib.SMTP("smtp.gmail.com",587) as connection:
      connection.starttls()
      connection.login(user = MY_EMAIL,password=MY_PASSWORD)
      connection.sendmail(
           from_addr = MY_EMAIL,
           to_addrs = "suryamuchhamarri@gmail.com",
           msg="Subject:Happy Birthday\n\n"
                )

'''



import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    smtp_server = 'smtp.gmail.com'
    port = 587
    login = 'arrakis025@gmail.com'
    password = 'ppkk lils dndd qoqk'  # Replace with your actual password or use an app-specific password if 2FA is enabled
    message = f"""
    <h3>New Feedback Submission</h3>
    <ul>
        <li>Customer: {customer}</li>
        <li>Dealer: {dealer}</li>
        <li>Rating: {rating}</li>
        <li>Comments: {comments}</li>
    </ul>
    """

    sender_email = login
    receiver_email = 'suryamuchhamarri@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")
