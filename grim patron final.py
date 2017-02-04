patron=[3]
newpatron=[]
j=0;
for wind in range(20):
    for i in range(wind):
        for p in range(0,len(patron)):
            patron[p]-=1
            if patron[p]>0:
                newpatron.append(3)
        i+=1
        patron=patron+newpatron
        newpatron=[]
    for p in range(0,len(patron)):
        if patron[p]<=0:
            j+=1
    i=0
    p=0
    j=0
    print(len(patron)-j)
