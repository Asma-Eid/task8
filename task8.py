print('Question (1):')
names= ["Tarteel","Asmaa","Ahmed"]
names.insert(0,"Sabrin") #(a)
print(names)
names.pop()              #(b)
print(names)
names.append("Hamda")    #(c)
print(names)
del names[2]             #(d)
print(names)

print('Question (2):')
friends = ['Adel','Ahmed']
employees = ['Samah','Amjad']
school = ['Ali','Basma']
list = friends + employees + school
print(list)

print('Question (3):')
dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}
dic = {**dic1, **dic2, **dic3}
print(dic)


print('Question (4):')
diction = {}
for i in range (1,16):
    diction[i] = i**2
print(diction)


print('Question (5):')
d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':150, 'b':200, 'd':400}
for key in d2:
    if key in d1:
        d1[key] +=d2[key]
    else:
        d1[key] = d2[key]
print(d1)


print('Question (6):')
Keys = ['Ten','Twenty','Thirty']
Values = [10,20,30]
dictionary = dict(zip(Keys,Values))
print(dictionary)


print('Question (7):')
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
                "marks": {
                   "physics": 70,
                   "history": 80
            }
       }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])



print('Question (8):')
myDict = {1:'Alaa',5:'Hadeel',7:'Hanin',13:'Malak'}
for key in myDict:
    if key<10 :
        print(myDict[key],end='->')

