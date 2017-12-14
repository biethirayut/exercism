def sum_of_multiples(limit, multiples):
    return sum(set([l for l in range(limit) for m in multiples if l % m == 0]))

