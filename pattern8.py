#n=int(input("enter the number : "))
n=5
for i in range(n,0,-1):
    print("-",end="")
    for j in range(n-i):
        print("-",end="")
    for k in range(1,i*2):
        print("*",end="")
    print()