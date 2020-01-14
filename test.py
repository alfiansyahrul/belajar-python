n = int(input("Enter Numbr :"))
for i in range ((-n)+1,n):
    t=n-abs(i)
    print(" "*(n-t), end=" ")
    for j in range(1,t+1):
        print(j,end=" ")
    print("")