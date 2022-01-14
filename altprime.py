from sys import argv

try:
    stNum = int(argv[1])
    enNum = int(argv[2])

    for x in range(int(stNum),int(enNum)):
        prime_flag = True
        for y in range(2,x):
            if (x%y)==0:
                prime_flag = False
                break

        if prime_flag == False:
            print(x, " is NOT a Prime.")
        else:
            print(x, " IS a prime.")
except IndexError:
    print("Need starting an ending numbers.")