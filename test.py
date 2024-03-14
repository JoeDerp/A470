

length = 10
def make(a,i):
    return 1+i**5

list = [make(5,i+1) for i in range(length)]
print(list)
list2 = [list[0]]
for i in range(1,len(list)):
    list2.append(list[i]-list[i-1])
print(list2)
list3 = [l/2 for l in list2]
list3.append(69)
print(list3)
print(min(list3))