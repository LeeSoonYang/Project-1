# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:44:52 2020

@author: keroy
"""
yy = 2020
mm = 2

month ={1:'January', 2:'February', 3:'March', 
		4:'April', 5:'May', 6:'June', 7:'July', 
		8:'August', 9:'September', 10:'October', 
		11:'November', 12:'December'} 

# code below for calculation of odd days -> number of days to move for 1st day of the year
day =(yy-1)% 28 #cycle finishes in 28 years, check if prv yr is leap yr

day = ((day) - (day)//4) + ((day)//4)*2 -2
#clock for leap year, must be divisible by 4, and if by 100,by 400

day = day % 7
print(day)

nly =[31, 28, 31, 30, 31, 30, 
	31, 31, 30, 31, 30, 31] 
ly =[31, 29, 31, 30, 31, 30, 
	31, 31, 30, 31, 30, 31] 
s = 0

if yy % 4 == 0: 
	for i in range(mm-1): #range starts from 0 and exclude last number as not in index
		s+= ly[i] 
else: 
	for i in range(mm-1): 
		s+= nly[i] 

day += s % 7 #remove number of previous weeks, give no of extra days
#number of days move by day 1 plus no of extra days for month of interest
day = day % 7
print(day)

# variable used for white space filling 
# where date not present 
space ='' 
space = space.rjust(2, ' ') 
print(space)

# code below is to print the calendar 
print(' '*2,month[mm], yy)
print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa') 

if mm == 9 or mm == 4 or mm == 6 or mm == 11: #only this months are 30
    if day == 6:
        for i in range(1,31):
           print("{:02d}".format(i), end =' ') 
           if i % 7 == 0: 
                print()
    else:
         for i in range(31 + day): 
                if i<= day: #if less than starting date leave blank
                    print(space, end =' ')
                    if (i + 1)% 7 == 0:
                        print() 
                else: 
                    print("{:02d}".format(i-day), end =' ') 
                    if (i + 1)% 7 == 0: 
                        print() 
elif mm == 2: 
    if yy % 4 == 0: #gregorian calender leap year is divisible by 4
        p = 30
    else: 
        p = 29
    if day == 6:
        for i in range(p):
            print("{:02d}".format(i), end =' ')
            print()
    else:
        for i in range(p + day):
            if i<= day: 
                print(space, end =' ')
                if (i + 1)% 7 == 0: 
                    print() 
            else: 
                print("{:02d}".format(i-day), end =' ') 
                if (i + 1)% 7 == 0: 
                    print() 
else: 
    if day == 6:
        for i in range(1,32):
           print("{:02d}".format(i), end =' ') 
           if i % 7 == 0: 
                print() 
    else:
        for i in range(32 + day):
            if i<= day:
                print(space, end =' ')
                if (i + 1)% 7 == 0: 
                    print() 
            else: 
                print("{:02d}".format(i-day), end =' ') 
                if (i + 1)% 7 == 0: 
                    print() 