import random
n=2
for i in range(0,10,1):
    otp=random.randint(10**(n-1),(10**n)-1)
    print(otp)
