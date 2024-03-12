import datetime as dt
today=dt.datetime.now()
today1=today.strftime("%Y"+"%m"+"%d")
today2=today.strftime("%H"+"%M"+"%S")
print(today1)
print(today2)
