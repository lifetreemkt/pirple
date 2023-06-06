def topseller (tvs, consoles, tablets):
    if tvs > consoles and tvs > tablets:
        print ('tv is the topseller')
    elif consoles > tvs and consoles > tablets:
        print ('consoles is the topseller')
    else:
        print ('tablet is the topseller')
        
topseller (120, 220, 115)