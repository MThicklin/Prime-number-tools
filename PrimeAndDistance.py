stNum = input("Starting number? ")
enNum = input("Ending number? ")

lasnum = 0
disAvg = 0
primeAvg = 0 
count = 0

f = open("PrimeNumbers.txt", "w")
f.write("The Primes between " + stNum + " & " + enNum +" are:\n")

for x in range(int(stNum),int(enNum)):
    prime_flag = True
    for y in range(2,x):
        if x%y==0:
            prime_flag = False
            break

    if prime_flag == False:
        continue
    else:
        distance = x - lasnum
        disAvg += distance
        primeAvg += x
        count += 1
        f.write(str(x)+"  - Distance from "+ str(lasnum) +": "+str(distance)+"\n")
        lasnum = x

f.write("Prime Average: "+ str(primeAvg/count) +" / Distance Average: "+str(disAvg/count))
f.close()