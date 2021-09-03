import csv
from collections import Counter

a= open('SOCR-HeightWeight.csv',newline='')
b = csv.reader(a)
fileData=list(b)
fileData.pop(0)

list=[]
for i in range(len(fileData)):
    num = fileData[i][2]
    list.append(float(num))

store=len(list)
list.sort()
total=0
#print(list)

for i in list:
    total=total+i
mean=total/store
print(mean)

if store%2 == 0:
    num1=float(list[store//2])
    num2=float(list[store//2-1])
    med=(num1+num2)/2
    print(med)
else:
    med=list[store//2]
    print(med)

mode=Counter(list)
rang={
    '75-85':0,
    '85-95':0,
    '95-105':0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0,
    '165-175':0,
}
#print(mode)

for i,y in mode.items():
    if 75<float(i)<85:
        rang['75-85']+=y
    elif 85<float(i)<95:
        rang['85-95']+=y
    elif 95<float(i)<105:
        rang['95-105']+=y
    elif 105<float(i)<115:
        rang['105-115']+=y
    elif 115<float(i)<125:
        rang['115-125']+=y
    elif 125<float(i)<135:
        rang['125-135']+=y
    elif 135<float(i)<145:
        rang['135-145']+=y
    elif 145<float(i)<155:
        rang['145-155']+=y
    elif 155<float(i)<165:
        rang['155-165']+=y
    elif 165<float(i)<175:
        rang['165-175']+=y
   
   

moder=0
modeo=0

for i,y in rang.items():
    if y>modeo:
        moder,modeo = [int(i.split('-')[0]),int(i.split('-')[1])],y

modevalue= float((moder[0]+moder[1])/2)
print(modevalue)
    
