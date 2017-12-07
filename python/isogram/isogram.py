def is_isogram(string):
    # string = string.lower()
    # a = []
    # b = 'abcdefghijklmnopqrstuvwxyz'
    # if len(string) < 1:
    #     return True
    # for char in string:
    #     if string.count(char) > 1 and char != ' ':
    #         a.append(char)
    #     elif string.count(char) > 1 and char == ' ':
    #         a.append(char)
    #
    # x = 0
    # y = 0
    # for i in a:
    #     for j in i:
    #         if j not in b:
    #             x += 1
    #         else:
    #             y += 1
    #
    # if (x > 1 and y > 1) or (x == 0 and y > 1):
    #     return False
    #
    # else:
    #     return True

    string = string.lower().replace(' ', '').replace('-', '')
    return True if len(set(string)) == len(string) else False
