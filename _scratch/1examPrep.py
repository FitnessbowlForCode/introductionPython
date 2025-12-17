from importFunctions import fString
import importFunctions as functions
i = 1
j = "Hallo"
while i <= 10:
    print("Ich bin gerade i", i)
    i += 1
else:
    print("i ist größer/gleich 10")

print(type(i))

fString(j)
functions.yInteger(2)

print(__name__)

def devByZero(x,y):
    try:
        a = x / y
        return a
    except ZeroDivisionError as ShittyError:
        return(print("Error Message! ", ShittyError))


devByZero(10,0)

val = 1.23456
print(f"Ergebnis: {val:4.2f}")
print(f"Ergebnis: {val:5.2f}")


a = 0

while a < 10:
    print(a % 2)
    a += 1
