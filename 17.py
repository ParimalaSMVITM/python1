import datetime as dt
today=dt.datetime.now()
y1=today.year
M1=today.month
d1=today.day
h1=today.hour
m1=today.minute
s1=today.second
#out1_20240227_053500.txt
fname1="out1_"
fname2=str(y1)+str(M1).zfill(2)+str(d1).zfill(2)+"_"+str(h1).zfill(2)+str(m1).zfill(2)+str(s1).zfill(2)
fname3=".txt"
fname=fname1+fname2+fname3
print(fname)
