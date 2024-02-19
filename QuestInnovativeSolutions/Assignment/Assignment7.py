#number to words
a=['zero','one','two','three','four','five','six','seven','eight','nine']
b=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c=['zero','ten','tewenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
n=int(input("Enter the number "))
if n<10:
    print(a[n])
elif n<20:
    n=n%10
    print(b[n])
elif n<100:
    x=n%10
    y=n//10
    if x!=0:
        print(c[y],a[x])
    else:
        print(c[y])
elif n==100:
    print("hundred")
elif n<1000:
        w=n//100
        x=n%100
        y=x//10
        z=x%10
        if w!=0 and x==0:
            print(a[w],'hundred')
        elif w!=0 and x<10:
            print(a[w],'hundred and',a[z])
        elif w!=0 and x<20:
            print(a[w],'hundred and',b[z])
        elif w!=0 and x<100:
            if z==0:
                print(a[w],'hundred and',c[y])
            else:
                print(a[w],'hundred and',c[y],a[z])      
elif n==1000:
    print("Thousand")    
else:
    print("Entered number is exceeded thousand")   
