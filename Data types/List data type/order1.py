list = [11,33,11,22,44,66,99,55,33,22,11]
list1 = []

while list:
    min = list[0] 
    for x in list: 
        if x < min:
            min = x
    list1.append(min)
    list.remove(min)    

print(list1)

