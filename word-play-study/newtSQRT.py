def newtSQRT(a):
    x = a - 1
    epsilon = 0.0000001
    while True:
        print(x)
        y = (x + a/x)/2
        if abs(y-x) < epsilon: 
            break
        x = y
    return y

