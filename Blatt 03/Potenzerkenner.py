
# Variable declaration (user input)
base = int(input("Enter a base: "))
n = int(input("Enter outcome: "))

# For testing purposes
# base = 2
# n = 25

def Potenzerkenner(base,n):
    # declare i as counting variable
    i = 1
    while i <= n:
        if((base ** i) == n):
            print("The desired number is", i)
            return i
        else: i += 1;
    print("No solution could be found!")

def PotenzAndBase(n):
   base = 0
   exponent = 0
   for base in range(0, (n+1)):
       for exponent in range(0,(n+1)):
           if ((base ** exponent) == n):
               print("%d ^ %d" %(base, exponent))

           else:
            continue


Potenzerkenner(base, n)
# PotenzAndBase(n)