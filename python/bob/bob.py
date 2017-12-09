def hey(phrase):
    if phrase.strip() == "":
        return 'Fine. Be that way!'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase.strip()[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'



"""
Bob answers 'Sure.' if you ask him a question.

He answers 'Whoa, chill out!' if you yell at him.

He says 'Fine. Be that way!' if you address him without actually saying anything.

He answers 'Whatever.' to anything else.
"""
