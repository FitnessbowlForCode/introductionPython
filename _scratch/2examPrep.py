l = ["Hello World!"]
print(type(l))
l = ()
print(type(l))

l = [1,2,3,4,5,6,7,8,9,10,12,11]
def inPlaceOpertations(x):
    return print(sorted(x))
inPlaceOpertations(l)

a = [1,2]
b = a
b[0] = 3
print(a[0])

list1 = [1,2,3]
listassign = list1
listcopy = list1.copy()
list1.append(4)
print(list1)
print(listassign)
print(listcopy)

a = list1 is listassign
print(a)
a = list1 is listcopy
print(a)
listcopy.append(4)
a = list1 is listcopy
print(a)
print(listcopy)

a = list1 == listassign
print(a)
a = list1 == listcopy
print(a)

list3 = [1, 2, ["a", "b", "c", ["a","s"]], 3]
list3[2][3].append(1)
print(list3)

import copy

list3 = [1, 2, ["a", "b"], 3]

# Echte tiefe Kopie
echte_kopie = copy.deepcopy(list3)

# Wir ändern die KOPIE
echte_kopie[2].append("X")

# Das Original bleibt sicher und unverändert
print(list3)       
# Ausgabe: [1, 2, ['a', 'b'], 3]  <-- Keine Änderung!

print(echte_kopie) 
# Ausgabe: [1, 2, ['a', 'b', 'X'], 3] <-- Nur hier ist das X

x = 12345
y = 12345
print(x is y)
x = 1.1
y = 1.1
print(x is y)

t = ("Hello", "World", "!")
a,b,c = t
print("a = {} and b = {} and c = {}".format(t[0],t[1],t[2]))
print("a = {} and b = {} and c = {}".format(a,b,c))

a = ["a", 2, 0.123, True]
print(a[:3])
a.insert(2,False)
print(a)
a.pop(2)
print(a)
print(a.index(0.123))

print(all(range(1,10)))
print(any(range(10)))

print(list("Hello World"))
a = "Hello"

lambda a:print(a, " World")