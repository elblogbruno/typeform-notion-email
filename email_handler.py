from smtplib import SMTP 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import os

def send_email_to_user(email, name):
    print('Sending email to {}'.format(email))
    env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))
    template = env.get_template('email-inlined.html')
    output = template.render(email=email, name=name)

    send_mail(output, email=email, name=name)    
    return "Mail sent successfully."

def send_mail(bodyContent, email, name):
    to_email = email
    from_email = str(os.environ["EMAIL_ADDRESS"])
    subject = 'Thanks for enrolling on the beta list of the Glassear SDK {0}!'.format(name)
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email

    message.attach(MIMEText(bodyContent, "html"))
    msgBody = message.as_string()

    server = SMTP(host=str(os.environ["EMAIL_STMP_HOST"]), port=587)
    server.starttls()
    print('Logging in to mail server...')
    server.login(from_email, str(os.environ["EMAIL_PASSWORD"]))
    server.sendmail(from_email, to_email, msgBody)

    server.quit()