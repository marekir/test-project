'''changes for my-local-branch'''
a=[]
b=[]
while 1:
    nums = str(input())
    if nums == 'end':
        break
    else:
        a.append([int(i) for i in nums.split()])
        b.append([0 for i in range(len(nums.split()))])

for i in range(0, len(b)):
    for j in range(0, len(b[i])):
        b[i][j]= a[i][j-1] + a[i][j-len(b[i])+1] + a[i-1][j] + a[i-len(a)+1][j]

for i in range(0, len(b)):
    print(*b[i])
