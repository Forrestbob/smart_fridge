# Import smtplib for the actual sending function
import smtplib


msg = {}
msg['Subject'] = 'I like tacos'
msg['From'] = 'SmartFridge@smartfridge.com'
msg['To'] = 'forrestbob2000@gmail.com'

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

# Send the message via our own SMTP server, but don't include the
# envelope header.
try:
	s = smtplib.SMTP(host='localhost', port=1025)
	s.sendmail('forrestbob2000@gmail.com', ['forrestbob2000@gmail.com','4042164620@tmomail.net'], message)
	s.quit()
	print "Successfully sent email"
except SMTPException:
	print "Error: unable to send email"