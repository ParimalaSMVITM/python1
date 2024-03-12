def table1(n1,n2):
    
    start=n1
    end=n2
    for j in range(start,end+1,1):
        
        for i in range(1,11,1):
            print(j,i,j*i)
        print()
start=int(input("Enter starting number: "))
end=int(input("Enter ending number: "))
table1(start,end)
