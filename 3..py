def genotp(size,qty):


    import random
    n=size
    for i in range(0,qty,1):
        otp=random.randint(10**(n-1),(10**n)-1)
        print(otp)
bank1=input("Enter the name of the bank:")        
if(bank1=="HDFC"):
    genotp(6,10)      
elif(bank1=="ICICI"):
    genotp(4,10)
