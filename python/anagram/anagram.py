# def detect_anagrams(word, candidates):
#     arrt = []
#     for i in candidates:
#         c = 0
#         for j in word.lower():
#             if j in i.lower():
#                 c += 1
#         if len(word) == c and len(i) == c:
#             arrt.append(i.lower())
#     
#     return list(set(arrt))


def detect_anagrams(word, candidates):
    arrt = []
    for w in candidates:
        if letters(word) == letters(w) and word.lower() != w.lower():
            arrt.append(w)
    return arrt


def letters(check_word):
    check_word = check_word.lower()
    dict = {}
    for i in check_word:
        dict[i] = check_word.count(i)
    return dict

def detect_anagrams(anagram, words):
    return [word for word in words if letters(anagram) == letters(word) and word.lower() != anagram.lower()]


def letters(word):
    word = word.lower()
    return dict((letter, word.count(letter)) for letter in word)