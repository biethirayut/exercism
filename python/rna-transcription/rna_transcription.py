def to_rna(dna_strand):
    a = []
    for i in dna_strand:
        a.append(Check(i))
    return ''.join(a)


def Check(i):
    if i in 'GCTA':
        if i == 'G':
            return 'C'
        elif i == 'C':
            return 'G'
        elif i == 'T':
            return 'A'
        else:
            return 'U'
    else:
        raise ValueError
