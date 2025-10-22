def gerade( zahl):
    try: 
        if((zahl) % 2 == 0):
            return True
        else:
            return False
    except TypeError:
        print('War keine Zahl: ' + zahl)
        return False

gerade('gerade')

def schaltjahr( jahr):
    if(jahr % 400 == 0):
        return print("Modulo 400", True)
    elif(jahr % 100 == 0):
        return print("Modulo 100", False)
    elif(jahr % 4 == 0):
        return print(True)
    else:
        pass

schaltjahr(1595)