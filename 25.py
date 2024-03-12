f1=open("dictionary.txt","r")
f2=open("words_8.txt","w")
list1=f1.readlines()
len2=len(list1)
print(len2)
count8=0
for i in range(0,len2,1):
    word1=list1[i]
    len1=len(word1)
    if len1>=8:
        count8=count8+1
        f2.write(str(count8)+". "+word1)
f2.close()
