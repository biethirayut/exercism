def distance(strand_a, strand_b):
    c = 0
    if len(strand_a) != len(strand_b):
        raise ValueError
    else:
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                c += 1
        return c
