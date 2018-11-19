a = 'That dog\'s ass was asking for it'

print('Input a letter an i will tell you if it is in the above')
x = input()

def contains(x):
    counter = 0
    a = 'That dog\'s ass was asking for it'
    for letter in a:
        if letter in x:
            counter = counter + 1
    if counter == 0:
        return print(f'{x} is not in the sentence {a}')
    else:
        return print(f'{x} is in {a} {counter} times')
            
    
