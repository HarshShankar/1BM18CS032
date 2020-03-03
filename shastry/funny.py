f = open("final.txt","r")
con = f.read()

l = []
l = con.split("\n")

for i in l:
	#print type(i)
	r1 = "u\'"
	s1 = i.replace("[","")
	s2 = s1.replace("]","")
	s3 = s2.replace("u'","")
	s4 = s3.replace("'","")
	print s4


		

f.close()