print("Hello World")



cars = ["Ford", "Volvo", "BMW"]

print(cars)

cars.append("Ken")

print(cars)

x = len(cars)

print(x)

myString = "Car berry"

print(myString)

if "berry" in myString:
    print("Yes its in")
else:
    print("Noooooooo")
    
    
    
for i in cars:
    print(i)
    
    
#text = input("Whats your name: ")  # Python 3
#print(text)

def upperCase(myWord):
    return myWord.upper()
    
    
    
print(upperCase("ken is nice"))



i=0
while i<3:
    i+=1
    print("Im breaking")
    #break
    

def factorial(n):
    if n>=1:
        return n*factorial(n-1)
    else:
        return 1

print(factorial(10))



