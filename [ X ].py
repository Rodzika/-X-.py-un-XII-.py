#1.uzd
num = int(input("enter the numper of rows:"))
for i in range (num):
    for j in range (num):
        print("*",end=" ")
    print()
    
    
#3.uzd
num = int(input("enter the numper of rows:"))
for i in range (1, num+1):
    print(" "* (num-i)+"* "*i)
    