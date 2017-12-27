import shlex
import string


def abbreviate(words):
    my_list = []
    for word in shlex.shlex(words):
        if word[0] in string.ascii_letters:
            my_list.append(word[0].upper())
    return ''.join(my_list[0:4])




