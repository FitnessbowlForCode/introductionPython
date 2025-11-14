daten = (
    "Musterstrasse 3",
    "Musterstadt",
    "mustermaxi@besterserver.at",
    "Der Chef",
    "Superfirma",
    "MUSTERMAXI@BESTERSERVER.AT",
    "1234 Dorfstadt",
    "burgamoaster@gemeindeamt.at"
    )

freundliste = ("burgamoaster@gemeindeamt.at",)


def finalspam(daten, freundliste):
    # local variables
    l = []
    myset = set()

    # find e-mail, set to lower and add to l
    for i in daten:
        x = i.find("@")
        if x != -1:
            y = i.lower()
            l.append(y)
        else:
            pass
    print("List removed not valid e-mails: ", l)

    # remove duplicates
    lengthOfL = len(l)

    for i in range(0,lengthOfL):
        pop = l.pop()
        myset.add(pop)
    print("List removed duplicates: ", myset)

    # convert the set-list into an list-list, bc set-list sucks
    m = list(myset)

    # remove friendlistet e-mail
    for i in freundliste:
        for j in m:
            if i == j:
                m.remove(i)
            else:
                pass
    m.sort()
    print("Final list: ", m)

    return m


finalspam(daten, freundliste)
