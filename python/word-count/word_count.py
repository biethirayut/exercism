from collections import Counter


def word_count(phrase):
    a = phrase.lower()
    b = []
    for i in a:
        b.append(i) if i.isalpha() or i.isdigit() or i == "'" else b.append(' ')

    x = ''.join(b).split()
    print(Counter(x))
    return Counter(x)



