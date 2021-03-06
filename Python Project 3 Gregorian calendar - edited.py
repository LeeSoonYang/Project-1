from JulianCalendar import julian_c

while True:
    try:
        yy = int(input("Enter year in yyyy format: "))
        if yy < 2020:
            print('Please enter a year at or after 2020!')
        else:
            print("year: ", yy)
            break
    except:
        print('Input is not a number!')

while True:
    try:
        mm = int(input("Enter year in mm format: "))
        if mm <= 0 or mm >= 13:
            print('Please enter a valid month!')
        else:
            print("month: ", mm)
            break
    except:
        print('Input is not a number!')
                       
    
month ={1:'January', 2:'February', 3:'March', 
		4:'April', 5:'May', 6:'June', 7:'July', 
		8:'August', 9:'September', 10:'October', 
		11:'November', 12:'December'} 
# code below for calculation of odd days 
day =(yy-1)% 400 #cycle finishes in 400 years, check if prv yr is leap yr

day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2 
#clock for leap year, must be divisible by 4, and if by 100,by 400

day = day % 7

nly =[31, 28, 31, 30, 31, 30, 
	31, 31, 30, 31, 30, 31] 
ly =[31, 29, 31, 30, 31, 30, 
	31, 31, 30, 31, 30, 31] 
s = 0

if yy%400 == 100 or yy%400 == 200 or yy%400 == 300: 
    for i in range (mm-1):
        s+=nly[i]
elif yy % 4 == 0: 
	for i in range(mm-1): #range starts from 0 and exclude last number as not in index
		s+= ly[i] 
else: 
	for i in range(mm-1): 
		s+= nly[i] 

day += s % 7 #remove number of previous weeks, give no of extra days
day = day % 7

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
    if yy%400 == 100 or yy%400 == 200 or yy%400 == 300: 
        p = 29
    elif yy % 4 == 0: #gregorian calender leap year is divisible by 4
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

jul = str(input("Display Julian Calendar? (Y/N)"))
if jul == 'Y':
    julian_c(yy,mm)
else:
    pass