def next_even_fib_after_N(n):
    x = 1
    y = 1
    result = [1,1]

    for i in range(1,9):
        temp = y + x
        result.append(temp)
        x = temp
        y = temp - y
    
    print(result)

    z = 3

    while(z % 2 != 0):

        z = result[n]    
        print(z)
        n += 1
        print(z)

    return print("Das ist das Ergebnis: ", z)
next_even_fib_after_N(6)
