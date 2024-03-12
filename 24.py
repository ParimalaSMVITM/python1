f1=open("dictionary.txt","r")
f2=open("words_8.txt","w")
for i in range(0,100,1):
    word1=f1.readline()
    len1=len(word1)
    if len1>=8:
        print(word1)
        f2.write(word1)

f2.close()
