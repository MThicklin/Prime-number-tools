for x in range(2,10):
    for y in range(2,x):
        if x%y==0:
            break
        else:
            print(x, " is a prime.")