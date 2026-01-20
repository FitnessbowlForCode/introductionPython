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

def costupdate(consumption, dept, purchasecost):
    for person in list(consumption.keys()):
 
        for product in list(consumption[person].keys()):
            if product in purchasecost:
                amount = consumption[person][product]
                price = purchasecost[product]
 
                if person not in dept:
                    dept[person] = 0
 
                dept[person] += amount * price
                del consumption[person][product]
        
        if not consumption[person]:
            del consumption[person]

costupdate(consumption, dept, purchasecost)