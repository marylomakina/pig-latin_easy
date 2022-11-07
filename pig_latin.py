def pig_latin(mystrig):
    word = mystrig.lower()
    if word[0] in 'aoeyui':
        return word+'ay'
    return word[1:]+word[0]+'ay'
