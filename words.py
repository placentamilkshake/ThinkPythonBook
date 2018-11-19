def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def writeNoE():
    fin = open('words.txt')
    f = open('wordsNoE.txt','w')
    for line in fin:
        word = line
        if has_no_e(word) == True:
            f.write(word)
    f.close()

def forbidden(word, nono):
    for letter in word:
        if letter in nono:
            return False
    return True

def writeForbidden():
    fin = open('words.txt')
    f2 = open('forbidden.txt', 'w')
    print('Input a letter: ')
    no = input()
    counter = 0
    for line in fin:
        word = line
        if forbidden(word, no) == True:
            counter = counter + 1
            f2.write(word)
    f2.close()
    fin.close()
    print(f'There are {counter} words that do not contain {no}.')

def uses_only(word, yes):
    for letter in word:
        if letter not in yes:
            return False
    return True

def writeOnly():
    fin = open('words.txt')
    f3 = open('usesOnly.txt', 'w')
    print('Input a series of letters: ')
    only = input()
    for line in fin:
        word = line.strip()
        if uses_only(word, only) == True:
            f3.write(word+'\r\n')
    f3.close()
    fin.close()

def uses_all(word, must):
    for letter in must:
        if letter not in word:
            return False
    return True

def writeReq():
    fin = open('words.txt')
    f4 = open('usesAll.txt', 'w')
    print('Input the letters that must be in the word: ')
    must = input()
    for line in fin:
        if uses_all(line, must) == True:
            f4.write(line)
    f4.close()
    fin.close()

def is_abecederian(word):
    previous = word[0]
    for i in word:
        if i < previous:
            return False
        previous = i
    return True

def writeOrder():
    fin = open('words.txt')
    f5 = open('ordered.txt', 'w')
    for line in fin:
        word = line.strip()
        if is_abecederian(word):
            f5.write(word+'\r\n')
    f5.close()
    fin.close()
