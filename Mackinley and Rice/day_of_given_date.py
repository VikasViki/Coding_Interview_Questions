date = input('Enter the Date (DD Mon YYY): ')
d,m,y = date.split()

day = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',
       4:'Thursday',5:'Friday',6:'Saturday'}

month = {'Jan':0,'Feb':3,'Mar':3,'Apr':6,
         'May':1,'Jun':4,'Jul':6,'Aug':2,
         'Sep':5,'Oct':0,'Nov':3,'Dec':5}
year = {(1600,1699):6,(1700,1799):4,(1800,1899):2,
        (1900,1999):0,(2000,2099):6}

val1 = int(d)
val2 = int(y[2:])
val3 = val2//4
val4 = month[m]
y = int(y)
val5 = 0
for key in year.keys():
  if key[0] <= y <= key[1]:
    val5 = year[key]
    break
#print(val1,val2,val3,val4,val5)
ans = val1+val2+val3+val4+val5

print(date,'is on', day[ans%7])
