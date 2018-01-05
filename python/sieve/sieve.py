def sieve(limit):
    list_prime = []
    for i in range(0, limit + 1):
        if (i % 2 != 0 or i == 2) and i >= 2:
            count = 0
            for j in range(1, i):
                if i % j == 0:
                    count += 1
            if count < 2:
                list_prime.append(i)
    return list_prime

