'''lst=[int(i) for i in input().split()]
n=int(input())
if lst.count(n)==0:
    print('Отсутствует')
else:
    for i in range(0,len(lst)):
        if lst[i]==n:
            print(i, end=' ')'''
n = int(input())
a = [[0 for i in range(n)]for i in range(n)]
step = 1
n1 = 0


while step<=n**2:
    for i in range(0+n1,n-n1):
        a[n1][i]=step
        step+=1    
    for i in range(n1+1,n-n1):
        a[i][n-n1-1]=step
        step+=1
    for i in range (n-n1-1,n1,-1):
        a[n-n1-1][i-1]=step
        step+=1
    for i in range (n-n1-2,n1,-1):
        a[i][n1]=step
        step+=1
    n1+=1
    #break
    
    #step+=1
'''for i in range (0,n):
    for j in range(0,n):
        a[j][i]=step
        step+=1'''
        
for i in range(0,n):
    print(*a[i])
    
