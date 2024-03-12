def table1(n1,n2):
    start=n1
    end=n2
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()

f1=open("in2.txt","r")
temp1=f1.readline().replace("\n","")
list1=temp1.split(",")
print(list1)
start=int(list1[0])
end=int(list1[1])
table1(start,end)
