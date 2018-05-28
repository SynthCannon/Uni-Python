##Nicholas Sumner 
#9/10/12

#Wk2Ex1:
list1=['Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon','Nitrogen','Oxygen','Flourine','Neon']
list2=['Sodium','Magnesium','Aluminium','Silicon','Phosphorus','Sulphur','Chlorine','Argon','Potassium','Calcium']
print 'list1 holds:',list1
print 'list2 holds:',list2
list1=list1+list2
print 'After concatenating the 2, list1 is now',list1

#append third part of list
list1.append('Scandium')
list1.append('Titanium')
list1.append('Vanadium')
list1.append('Chromium')
list1.append('Manganese')
list1.append('Iron')
list1.append('Cobalt')
list1.append('Nickel')
list1.append('Copper')
list1.append('Zinc')

#outputs
print 'After adding the next 10 elements, list1 is:',list1
print 'The amount of Elements in List 1 is',len(list1)
print 'The 23rd Element is',list1[22]

#Wk2Ex1b
y=0
FourLetWord=[0,0,0]
for x in range(0,30): #in range 0->30 of list1, repeat
    if list1[x][0]=='S': #is first character 'S'?
        print x, list1[x] #print if correct
        
    if len(list1[x])==4:#if string in list1 is of length 4, then
        FourLetWord[y]=list1[x]#array of 4 letter words
        y+=1#increment y for next element to be put into FourLetWord
print 'the only 4 elements with 4 letters in the 1st 30 elements are:',FourLetWord






import array
import timeit
list=range(1000000)

t = timeit.Timer(""list+1"")
print t.timeit(1)
