import smtplib
from email.mime.text import MIMEText

# email details
subject = "Automated Rejection"
body = "Hello, \n I regret to inform you that you have not been selected for this position. The reasons are as follows: "
reasons = ["This was a ghost job.", "You resume did not pass our scanning pre-select screening from whatever program we use to scan resumes.", "We'd already selected somebody for the role but had to post it for legal reasons.", "There was an actual reason why you weren't selected." ]
recipients = ["person1@example.com", "person2@example.com"]
password = "N07_7H47_345Y"

def send_email(subject, body, reasons, input):
    msg = MIMEText(body + reasons[input])
    msg['Subject'] = subject
    msg['From'] = sender
    msg['to'] = ','.join(recipients)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as stmp_server:
    smtp_server.login(sender,password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Email successfully sent")


reason_input = ("Why are they being rejected? ")
send_email(subject, body, reasons, reason_input)