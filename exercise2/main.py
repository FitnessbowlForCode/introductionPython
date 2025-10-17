#start working here
def verzollen( warenwert):
    if(warenwert >= 150):
        return warenwert * 1.37
    elif(warenwert > 22):
        return warenwert * 1.2
    else:
        return warenwert

verzollen(22)

def bmi( mass, height):
    BMI = mass/(height * height)
    if(BMI < 18.5):
        return ("Untergewicht")
    elif(BMI <= 25.0):
        return ("Normalgewicht")
    elif(BMI <= 30.0):
        return ("Übergewicht")
    else:
        return ("Adipositas")

bmi(75,1.75) #bmi(mass,height)