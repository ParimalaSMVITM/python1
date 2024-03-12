def table1(n1,n2):
    
    start=n1
    end=n2
    f2=open("in2.txt","w")

    for j in range(start,end+1,1):
        
        for i in range(1,11,1):
            a=i("*"
            print(j,i,j*i)
            
            f2.write(str(table1(int(n1),int(n2))))
        print()
f1=open("in1.txt","r")
info1=f1.readlines()
n1=info1[0].replace("\n","")
n2=info1[1].replace("\n","")
f2=open("in2.txt","w")
f2.write(str(table1(int(n1),int(n2))))
f2.close()
