consumption = {
    'Franz': {
        'Kaffee': 7,
        'Zucker': 7,
        'Milch': 7,
        'Schoki': 3,
        },
    # 'Franziska': {
    #     'Kaffee': 3,
    #     'Tee': 5,
    #     'Zucker': 4,
    #     'Kekse': 1,
    #     },
}

dept = {
    'test': 1
    }

purchasecost = {
    'Kaffee': 0.25,
    'Tee': 0.2,
    'Zucker': 0.1,
    'Schoki':0.5,
    'Kekse': 1.25
}

def costupdate( consumption, dept, purchasecost):
    costList = []
    for x,y in consumption.items():
        print("I'm key:",x,'\n' ,"I'm value" , y, '\n')

        for a, b in list(y.items()):
            print("I'm key:",a,'\n' ,"I'm value" , b, '\n')

            for c, d in purchasecost.items():
                if a == c:
                    costList.append(d*b)
                    del y[a]

    print(sum(costList))
    print(consumption)
costupdate( consumption, dept, purchasecost)