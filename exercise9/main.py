def encode(text, code_table, usecaps=True, insep="", outsep=" "):

    if usecaps:
        text = text.upper()

    if insep == "":
        parts = list(text)
    else:
        parts = text.split(insep)
    
    encoded_parts = []
    for part in parts:
        if part in code_table:
            encoded_parts.append(code_table[part])
            
    return outsep.join(encoded_parts)


def combinecodetable(ct1, ct2):
    ct3 = {}
    
    for key1, val1 in ct1.items():
        for key2, val2 in ct2.items():
            if val1 == key2:
                ct3[key1] = val2    
    return ct3