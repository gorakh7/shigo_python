s = {10,20,30}
s.add(40)
print(s)
s.add(20)
s1 = {40,50,20,20,50}
s.update(s1,range(5))
print(s)
s2 = s.copy()
print(s2)
print(s2.pop())
