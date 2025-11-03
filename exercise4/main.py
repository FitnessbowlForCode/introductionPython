def zahlentyp(zahl):
    teiler = [1]

    for i in range(2, zahl // 2 + 1):
        if zahl % i == 0:
            teiler.append(i)
        else:
            pass

    teilersumme = sum(teiler)

    print(f"Teiler von {zahl}: {teiler}")
    print(f"Summe der Teiler: {teilersumme}")

    if teilersumme < zahl:
        return print("defizient")
    elif teilersumme > zahl:
        return print("abundant")
    else:
        return print("vollkommen")

zahlentyp(12)
