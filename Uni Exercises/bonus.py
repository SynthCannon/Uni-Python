import urllib2
#skip 418 chars
#import numarray

#define the url link
try:
	website = urllib2.urlopen('http://www.metoffice.gov.uk/climate/uk/stationdata/heathrowdata.txt')
except urllib2.HTTPError, e:     
	print "Cannot retrieve URL: HTTP Error Code", e.code
except urllib2.URLError, e:     
	print "Cannot retrieve URL: " + e.reason[1] 

#put useable data into heatTxt as string
heatTxt2= website.read()
heatTxt=heatTxt2[417:len(heatTxt2)] #char 418 is where useable data starts

#count amount of sets of values in data
lineCount=0
for y in range(0,len(heatTxt)):
	if heatTxt[y]=='\n':
		lineCount+=1


#array=zeros((lineCount,7))

takingIn=False #indicates whether characters are being put into the input string or not
falseBool=False #indicates when to stop putting characters into the string
bool2=False
field=0 #which field of data is being put in
dataSet=0
string=[] #hold data as list
stringChar=0
array=[7,lineCount]



for x in range(0,len(heatTxt)): #Without array input
	
	if heatTxt[x]=='-' and (field==4 or field==6):
		falseBool=True
		
	elif heatTxt[x]!=" " and heatTxt[x]!="-" and heatTxt[x]!="#" and heatTxt[x]!='\n' and falseBool==False:
		string.append(heatTxt[x])
		if stringChar<5:
			stringChar+=1
			takingIn=True
		else:
			falseBool=True
	#elif falseBool==True and string[0]=='P' :
		#falseBool=
	
		
	elif (heatTxt[x]==' ' or heatTxt[x]=='#' or string==['P', 'r', 'o', 'v', 'i', 's']) and takingIn==True:
		print string,falseBool
		takingIn=False
		string=[] 
		stringChar=0
		if falseBool==True:
			falseBool=False
		else:
			if field==0:
				
			elif field==1:
				
			elif field==2:
				
			elif field==3:
				
			elif field==4:
				
			elif field==5:
				
			elif field==6:
				field=-1
				dataSet+=1
		field+=1		
	
	