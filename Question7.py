i = 1
num = 1
while (i <=5):  
    j = 1
    while (j <= i):
        if (i%2==0):
            print(num,end=' ')
        else:
            print(chr(num+64),end=' ')
        num+=1
        j+=1
    print()
    i+=1