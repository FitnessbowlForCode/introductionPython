try:
    file = open("todo.txt","rt")
    for line in file:
        print(line)
except:
    FileNotFoundError
    file = open("todo.txt","w+t")

todos = [ line.strip() for line in file]
file.close()

for line in todos:
    print(line)
print(todos)

MOD = False

if MOD:
    file = open("todo.txt","wt")
    for todo in todos:
        file.write(todo)
        print(todo, file=flo)
    file.close()