import smtplib

f = open("final.txt","r")
con = f.read()

l = []
l = con.split("\n")
fm=""
for i in l:
	#print type(i)
	r1 = "u\'"
	s1 = i.replace("[","")
	s2 = s1.replace("]","")
	s3 = s2.replace("u'","")
	s4 = s3.replace("'","")
	fm+=s4+"\n"


		
print fm
f.close()

server = smtplib.SMTP_SSL('smtp.zoho.in',port=465) #server for sending the email

server.ehlo() # simple starting of the connection
server.login('testbms@zohomail.in','testbms123') # login credentials and password

msg = """From:testbms@zohomail.in
Subject: Records \n
To: testbms@zohomail.in \n
"""
# This is where the email content goes. It could be information about the error, time of day, where in the script, etc.

server.sendmail('testbms@zohomail.in','testbms@zohomail.in',msg+fm) # this is where the email is sent to the recipient

server.quit() # exit the connection