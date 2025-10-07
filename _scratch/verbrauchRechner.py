def f(x,y):
    result = x % 100 * y
    return result

print("##############################################################")
print("--------------------Autoverbrauch-Rechner--------------------")
print("##############################################################")

print("Wie viel [Liter oder kwH] verbraucht dein Auto pro 100km? ")
_userInputL_kwH = input()
_userInputL_kwH_INT = float(_userInputL_kwH)
print(f"Wert: {_userInputL_kwH_INT}")
print()

print("Wie viel kostet der [Liter oder die kwH] in Euro? z.B. 1,60€ oder 0.20€")
_userInputPrice = input()
_userInputPrice_INT = float(_userInputPrice)
print(f"Wert: {_userInputPrice_INT}")
print()

result = f(_userInputL_kwH_INT,_userInputPrice_INT)

print(f"Der Betrag in {result}€ ")
