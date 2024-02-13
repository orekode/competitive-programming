def freqAlphabets(self, s: str) -> str:

    encs = []

    for i in range(17):
        encs.append(str(10 + i) + '#')
    for i in range(9):
        encs.append(str(i + 1))

    alphs = list("jklmnopqrstuvwxyzabcdefghi")


    for i in range(len(encs)):


        enc_type = encs[i]

        if enc_type in s:
            s = s.replace(enc_type, alphs[i])
    
    return s
    
