class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Function Hello, my name is {} and I'm {} years old".format(self.name,self.age))

  def __str__(self):
    return "__str__ Hello, my name is {} and I'm {} years old".format(self.name,self.age)

p1 = Person("Emil", 25)
p2 = Person('Angi', 21)

p1.greet()
p2.greet()

print(p1)