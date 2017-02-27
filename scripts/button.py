import RPi.GPIO as GPIO
import time
import smtplib	#email sending
from email.mime.text import MIMEText	#email modules
from email.MIMEMultipart import MIMEMultipart	#email modules

import MySQLdb

#mySQL config
db = MySQLdb.connect("localhost", "DataBAEs", "DataBAEs", "test")
curs=db.cursor()

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#email config
msg = MIMEMultipart()
msg['From'] = 'Smart Fridge'
msg['To'] = 'forrestbob2000@gmail.com'
msg['Subject'] = 'Automatic Order Placed'
message = 'Your smart fridge ordered you another pack of beer!'
msg.attach(MIMEText(message))
mailerhost = 'smtp.gmail.com'
mailerport = 587


	

while True:
	input_state = GPIO.input(18)
	if input_state == False:
		try: 
			curs.execute ("INSERT INTO `test`.`test_table` (`epochTime`) VALUES ('" + str(time.time()) + "')")

			db.commit()
			
			mailserver = smtplib.SMTP(mailerhost,mailerport)
			mailserver.ehlo()
			mailserver.starttls()
			mailserver.ehlo()
			
			mailserver.login('forrestbobtest@gmail.com', '123test123')
			mailserver.sendmail('forrestbobtest@gmail.com',['forrestbob2000@gmail.com'],msg.as_string())
			mailserver.quit()
			
			print "Data committed & email sent"
			
		except: 
			print "There was an error."
			db.rollback()
		time.sleep(0.2)
		
