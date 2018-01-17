import smtplib, random
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox


#Create widgets (root, labels, buttons, entries)
root = tk.Tk()
##### THIS CHANGES TEXT SIZE BUT NOT TO THE FONT SIZE INDICATED FIX THIS
root.option_add("*Font", 10)
#####
step1_lab = tk.Label(root, text = "1. Add participants' names, emails, and wishlists:")
step1_sublab = tk.Label(root, text = "(Don't forget your own information!)", font = ("TkDefaultFont", 10))
step2_lab = tk.Label(root, text = "2. Enter your Gmail credentials:")
step3_lab = tk.Label(root, text = "3. Send emails:")

new_but = tk.Button(root, text = "New")
edit_but = tk.Button(root, text = "Edit")
del_but = tk.Button(root, text = "Delete")
send_but = tk.Button(root, text = "Send")

email_ent = tk.Entry(root, text = "Email")
pass_ent = tk.Entry(root, text = "Password", show = "*")

#Format the widgets using the grid layout
step1_lab.grid(row = 0, column = 0)
step1_sublab.grid(row = 1, column = 0)
"""Placeholder for table"""
new_but.grid(row = 3, column = 0)
edit_but.grid(row = 3, column = 1)
del_but.grid(row = 3, column = 2)

step2_lab.grid(row = 5, column = 0)
email_ent.grid(row = 6, column = 0)
pass_ent.grid(row = 6, column = 1)

step3_lab.grid(row = 8, column = 0)
send_but.grid(row = 9, column = 0)


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
		msg.attach(MIMEText("Hello " + self.name + ",\n\n\tYou have been assigned " + self.recipient.name + " for Secret Santa. Here is their list:\n"))
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

def draw():
	#Check if anyone drew themselves
	unique = False

	#Pick random recipient for each person until everyone gets someone other than themselves
	while not unique:
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
	root.mainloop()
