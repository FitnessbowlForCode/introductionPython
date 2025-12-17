def cds2acid(cds):
    a = 0
    b = 3
    t = {}
    acids = {
        # U
        "UUU": "Phenylalanin", "UUC": "Phenylalanin",
        "UUA": "Leucin", "UUG": "Leucin",
        "UCU": "Serin", "UCC": "Serin", "UCA": "Serin", "UCG": "Serin",
        "UAU": "Tyrosin", "UAC": "Tyrosin",
        "UAA": "Stop", "UAG": "Stop",
        "UGU": "Cystein", "UGC": "Cystein",
        "UGA": "Stop", "UGG": "Tryptophan",

        # C
        "CUU": "Leucin", "CUC": "Leucin", "CUA": "Leucin", "CUG": "Leucin",
        "CCU": "Prolin", "CCC": "Prolin", "CCA": "Prolin", "CCG": "Prolin",
        "CAU": "Histidin", "CAC": "Histidin",
        "CAA": "Glutamin", "CAG": "Glutamin",
        "CGU": "Arginin", "CGC": "Arginin", "CGA": "Arginin", "CGG": "Arginin",

        # A
        "AUU": "Isoleucin", "AUC": "Isoleucin", "AUA": "Isoleucin",
        "AUG": "Methionin",
        "ACU": "Threonin", "ACC": "Threonin", "ACA": "Threonin", "ACG": "Threonin",
        "AAU": "Asparagin", "AAC": "Asparagin",
        "AAA": "Lysin", "AAG": "Lysin",
        "AGU": "Serin", "AGC": "Serin",
        "AGA": "Arginin", "AGG": "Arginin",

        # G
        "GUU": "Valin", "GUC": "Valin", "GUA": "Valin", "GUG": "Valin",
        "GCU": "Alanin", "GCC": "Alanin", "GCA": "Alanin", "GCG": "Alanin",
        "GAU": "Asparaginsäure", "GAC": "Asparaginsäure",
        "GAA": "Glutaminsäure", "GAG": "Glutaminsäure",
        "GGU": "Glycin", "GGC": "Glycin", "GGA": "Glycin", "GGG": "Glycin"
    }

    while b <= len(cds):
        codon = cds[a:b]
        
        if codon in acids:
            amino_name = acids.get(codon)
            
            t[amino_name] = t.get(amino_name, 0) + 1
            
        a += 3
        b += 3
    
    return t

print(cds2acid("UUGUUG"))