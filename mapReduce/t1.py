a = [(0, 33), (3, 26), (4, 95), (0, 28), (1, 12), (2, 3), (4, 69)]

sum=0
for i in range(len(a)):
    a1=a[i][1]
    b1=0
    for j in range(i,len(a)):
        if a[i][0]==a[j][0] and i!=j:
            b1=a[j][1]
            break			
    sum+=(a1*b1)		

print sum