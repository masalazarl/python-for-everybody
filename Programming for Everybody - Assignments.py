#Programming for everybody

#Assingment 2.3 
hrs = input("Enter Hours:\n")
rate_hrs = input("Rate per hours:\n") 
pay = float(rate_hrs)*float(hrs)
print("Pay:", pay)

#Excercise 5, chapter 2 - Celsius to farenheit 
print("Temperature Converter: Celsius to Farenheit")
cel = float(input("Enter a celsius temperature :\n"))
fahr = cel*1.8 + 32
print("Farenheit temperature: ", fahr)

#Example for using try and except
inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0  
    print(cel)
except:
    print('Please enter a number')

#Assignment 3.1 
hrs = float(input("Enter Hours:"))
rate_hrs = float(input("Enter Rate per Hours:"))
if hrs <= 40: 
    pay = hrs*rate_hrs
else: 
    pay = 40*rate_hrs + (hrs-40)*(1.5*rate_hrs)

print(pay)

#Assignment 3.3 
score = float(input("Enter Score: "))
if 0.0 <= score <= 1.0: 
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
else:
    print("error")

import random
t = [1,2,3,4,5,6]
random.choice(t)

#Assignment 4.6 

def computepay(h, r):
    if h <= 40: 
        return h*r
    elif h > 40: 
        return 40*r + (h-40)*(1.5*r)


hrs = float(input("Enter Hours:"))
rate_hrs = float(input("Enter Rate Per Hour:"))
p = computepay(hrs, rate_hrs)
print("Pay", p)

#Assignment 5.2

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try: 
        num = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or num > largest:
            largest = num
    if smallest is None or num < smallest:
            smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)

