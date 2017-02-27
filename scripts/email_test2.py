import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'Smart Fridge'
msg['To'] = 'forrestbob2000@gmail.com'
msg['Subject'] = 'Automatic Order Placed'
message = 'Your smart fridge ordered you another pack of beer!'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()

try:
	mailserver.login('forrestbobtest@gmail.com', '123test123')

	mailserver.sendmail('forrestbobtest@gmail.com',['forrestbob2000@gmail.com','4042164620@tmomail.net'],msg.as_string())

	mailserver.quit()
	print "Successfully sent email"
except:
	print "Error: unable to send email"