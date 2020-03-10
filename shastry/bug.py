file = open("records.txt","r")
contents = file.read()
y=[]
i=contents.split("\n")
for x in i:
	y.append(x.split("\t"))


i=0
for i in range(0,len(y)-1):
	if y[i] != y[i+1]:
		print y[i]
	else:
		pass
