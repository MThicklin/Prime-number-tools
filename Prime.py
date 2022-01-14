stNum = input("Starting number? ")
enNum = input("Ending number? ")

f = open("PrimeNumbers.txt", "w")
f.write("The Primes between " + stNum + " & " + enNum +" are: ")

for x in range(int(stNum),int(enNum)):
    prime_flag = True
    for y in range(2,x):
        if x%y==0:
            prime_flag = False
            break

    if prime_flag == False:
        continue
    else:
        f.write(str(x)+" ")