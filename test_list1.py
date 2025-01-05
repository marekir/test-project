'''a=[int(i) for i in input().split()]
b=0
for i in a:
    b+=i
print(b)'''
a=[int(i) for i in input().split()]
a.sort()
b=[]
if len(a)>1:
    for i, item in enumerate(a):
        if (a[i-1]==a[i] or a[i]==a[i-len(a)+1]) and a[i] not in b:
            b.append(a[i])
print(*b)
