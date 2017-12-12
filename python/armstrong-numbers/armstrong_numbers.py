def is_armstrong(number):
    number = str(number)
    sum = 0
    for i in number:
        print(i)
        sum += int(i) ** len(number)
    print(sum)
    return True if int(number) == sum else False
