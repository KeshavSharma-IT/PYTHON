# size = 5
# for x in range(size,-(size),-1):
#     for y in range(1,abs(x)+1):
#         print(" ",end="")
#     for z in range(size,abs(x),-1):
#         print("*",end="")
#     print()


n=7
m=n//2+1
for x in range(1,n+1):
    for y in range(1,n+1):
        if(y>=m)!=0 and y<=n-m+1:
            print("*",end="")
        else:
            print(" ",end="")
    if x<=n//2:
        m-=1
    else:
        m+=1
    print()