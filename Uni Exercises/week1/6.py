#file open
file=open('Y:\ph2150\Exercises\week1\ex6.txt','w+')
#write string to file
file.write("In all cases in which work is produced by the agency of heat, a quantity of heat is consumed which is proportional to the work done; and conversely, by the expenditure of an equal quantity of work an equal quantity of work an equal quantity of heat is produced")
file.seek(22)
print file.read(4)
file.seek(0)
str=file.read(255)
print str
file.close