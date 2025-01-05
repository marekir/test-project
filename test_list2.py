'''n_sum = 0
sq_sum = 0
while 1:
    n = int(input())
    n_sum += n
    sq_sum += n**2
    if n_sum==0:
        print(sq_sum)
        break'''

'''for i in range(0, int(input())+1):
    for j in range(0,i):
        print(i, end=' ')
'''
'''n=int(input())
cur=1
pr=1
while cur<=n and pr<=n:
    while cur<=n and pr<=n:
        print(cur, end=' ')
        pr+=1
    cur+=1'''
    
'''n = int(input())
a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a)'''
