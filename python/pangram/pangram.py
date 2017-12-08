def is_pangram(sentence):
    # sentence = sentence.replace(' ', '').replace('.', '').replace('"', '').replace('_', '')
    # sentence = set(sentence)
    # if len(sentence) == 26:
    #     return True
    # else:
    #     return False

    return True if len(set([x for x in sentence if str(x).isalpha()])) == 26 else False
a
