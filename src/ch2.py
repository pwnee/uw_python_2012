'''
Created on Oct 13, 2012

@author: wtb
'''
import math
#Exercise 2.3
print "Execise 2.3"
width = 17
height = 12.0
delimiter = '.'

a = width / 2 #answer = 8 
b = width / 2.0  #answer = 8.5
c = height / 3 #answer = 4.0
d = 1 + 2 * 5 #answer = 11
e = delimiter * 5 #answer = .....

print "Number 1:", a
print "Number 2:", b
print "Number 3:", c
print "Number 4:", d
print "Number 5:", e

#Exercise 2.4
#Number 1
print "Exercise 2.4"
volume = (4.0/3.0 *math.pi) * (5**3) 
print "Number 1: The volume of a sphere with radius 5 is", volume

#Exercise 2.4
#Number 2
price = 2495
discount = .40
copies = 60
price = price - (price * discount)
price = price * 60
shipping = 300 + (60 * 75)
shipping = shipping
total = price + shipping
total = '{0:.02f}'.format(float(total) / 100.0)
print "Number 2: The total wholesale cost for 60 copies is", total

#Exercise 2.4 
#Number 3
'''
leave at 6:52 AM
1 miles @ 8m15s
3 mi tempo @ 7m12s
1 mi ez 8m15s
'''
import datetime
def to_seconds(minutes, seconds):
    minutes = minutes * 60
    total_seconds = minutes + seconds
    return total_seconds

time = datetime.datetime(1,1,1,6,52,0)

easy_seconds = to_seconds(8,15)*2
tempo_seconds = to_seconds(7,12)*3
total_seconds = easy_seconds + tempo_seconds
breakfast_time = time + datetime.timedelta(0,total_seconds)
print "Number 3: You will arrive home for breakfast at", breakfast_time.time(), "AM.  Mmmm pancakes..."











