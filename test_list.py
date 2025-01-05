'''a=[int(i) for i in input().split()]
b=0
for i in a:
    b+=i
print(b)'''
'''added some changes_R'''
a=[int(i) for i in input().split()]
if len(a)==1:
    print(*a)
else:
    for i in range (0, len(a)):
        print(*[a[i-1]+a[i-len(a)+1]],' ', end='')
