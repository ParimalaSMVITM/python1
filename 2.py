def genotp(size,qty):
    
    import random
    n=size
    for i in range(0,qty,1):
        otp=random.randint(10**(n-1),(10**n)-1)
        print(otp)
genotp(4,10)
genotp(6,10)
