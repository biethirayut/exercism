import string


def rotate(text, key):
    output = ''
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    for char in text:
        if char in lowercase:
            output += lowercase[(lowercase.index(char) + key) % len(lowercase)]
        elif char in uppercase:
            output += uppercase[(uppercase.index(char) + key) % len(uppercase)]
        else:
            output += char
    return ''.join(output)
