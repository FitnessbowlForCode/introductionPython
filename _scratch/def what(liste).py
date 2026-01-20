def what(liste):
    for i in range(1, len(liste)):
        liste[i] += liste[i-1]
 
def showwhat(liste):
    print(liste)
    a, b, c, d = liste
    print( a+d < b+c )
 
l = [1,2,3,4]
what(l)
showwhat(l)
l.reverse()
a = 100 # Globales a = 100 hat keinen Einfluss auf lokale Zuweisung in showwhat
what(l)
showwhat(l)
