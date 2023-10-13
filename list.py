#Lists
luckey_num=[0,7,8,4,2,3,1]
friend=['Farjana','Ana','Mim','Tamanna','Hur','Jam']
#insert add new item
friend.insert(1,'Sadia')
print(friend)


print(friend[-1])
#print from 3 to last one
print(friend[3:])
# 5no. wont be printed
print(friend[2:5])
print(friend.index('Hur'))
#sorting (ascending)
friend.sort()
print(friend)
luckey_num.sort()
print(luckey_num)
#reversing (last to first not ascending)
luckey_num.reverse()
print(luckey_num)


#copying from another list
not_frnd=friend.copy()
print(not_frnd)


#[2], it replaces the item
friend[2]='Ani'
print(friend)
friend.extend(luckey_num)
print(friend)


matrix=[
    [3,5,7],
    [8,9,0],
    [2,1,4],
    [0]
]
print(matrix[1][1])
print(matrix[2][0])
for row in matrix:
    print(row)
for row in matrix:
    for col in row:
        print(col)


#square root
import math as n
x=n.sqrt(3)
print(x)
    