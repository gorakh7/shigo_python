def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
print(max([1,2,3,-8,0,9]))        