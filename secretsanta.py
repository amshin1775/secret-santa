import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = "***SENDER'S EMAIL ADDRESS"
signature = "***CUSTOM SIGNATURE"

class Participant:

	def __init__(self, name, email, lst, recipient = None):
		self.name = name
		self.email = email
		self.list = lst
		self.recipient = recipient

	def send_email(self):
		"""Sends email to the Participant with their assignment's name and list"""
		msg = MIMEMultipart()
		msg['From'] = from_addr
		msg['To'] = self.email
		msg['Subject'] = "Secret Santa info enclosed"

		#Setup the email message
		msg.attach(MIMEText("Hello Corpsman,\n\n\tYou have been assigned " + self.recipient.name + " for our 2017 Secret Santa. Here is their list:\n"))
		msg.attach(MIMEText(self.recipient.list, 'plain'))
		msg.attach(MIMEText(signature, 'plain'))

		#Send the email
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(from_addr, "***PASSWORD HERE")
		text = msg.as_string()
		server.sendmail(from_addr, self.email, text)
		server.quit()

partics = ["***LIST OF PARTICIPANTS"]

def main():
	#Check if anyone drew themselves
	unique = False

	#Pick random recipient for each person until everyone gets someone other than themselves
	while !unique:
		getters = list(partics)
		for partic in partics:
			getter = getters[random.randint(0, len(getters) - 1)]

			#Check if person picked themselves and other Participants exist
			while len(getters) > 1 and partic.name == getter.name:
				getter = getters[random.randint(0, len(getters) - 1)]
			
			partic.recipient = getter

			#Check if the last person got themself
			if len(getters) == 1:
                                if not partic.name == getter.name:
                                        unique = True
			getters.remove(getter)
			
	#Send each partic the email containing their assignment
	for partic in partics:
		partic.send_email()
	for getter in getters:
		print(getter.name)

if __name__ == "__main__":
	main()
