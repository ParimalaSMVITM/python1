def genotp(size,qty):


    import random
    n=size
    for i in range(0,qty,1):
        otp=random.randint(10**(n-1),(10**n)-1)
        print(otp)
banks=["HDFC","ICICI","SBI","HSBC"]
sizes=[6,4,5,8]
bank1=input("Enter the name of the bank:")
position=banks.index(bank1)

size1=sizes[position]

genotp(size1,10)
