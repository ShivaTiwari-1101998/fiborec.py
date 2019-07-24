n=int(input("Enter the no "))
c=0
while(True):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if(i%j==0):
                break
            c=c+1
    if(c==50):
        print("The first no. to have 50 factors:",i)
    break
