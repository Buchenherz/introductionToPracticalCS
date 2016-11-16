limit = 12000000 #int(input("Print prime numbers to: ")) # Whole number

flags = {}
for i in range(2, limit + 1):
    flags[i] = True

def getPrimes(limit):

    for p in range(2, limit+1):
        if flags[p] is True:
            print(p)
            m = p*p
            while m <= limit:
                flags[m] = False
                m += p

getPrimes(limit)
#while limit <= 1000000:
#    getPrimes(limit)
#    limit *= 10