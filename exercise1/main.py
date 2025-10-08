def f(x,y):
    if y == 0:
        return None
    else:
        return x/y

_result = f(10.0,2.0)

if _result == None: #if _result is None: <-- "pytonischere Schreibweise laut ChatGPT"
    print("Division durch 0 ist nicht erlaubt")
else:
    print(f"Das Ergebnis ist: {_result}")