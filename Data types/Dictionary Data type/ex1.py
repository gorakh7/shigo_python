rec={}

n=int(input("Enter no::"))
i=1
while i <=n:
    name=input("Enter student Name:")
    marks=input("Enter % of Marks of Student:")
    rec[name]=marks
    i=i+1
print("Name of Student","\t","% of marks")
for x in rec:
    print("\t",x,"\t\t",rec[x])    