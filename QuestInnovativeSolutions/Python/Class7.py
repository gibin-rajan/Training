# #printing 10 to 1

i=10
while i>0:
    print(i)
    i=i-1

#sum of 1 to 10 num using while loop

i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print("The sum of first 10 num is ",sum)

#while else
i=1
while i<=5:
    print(i)
    i+=1
else:
    print("finished")
    
    
#while break
i=1
while i<=5:
    if i==3:
        break
    print(i)
    i+=1
else:
    print("finished")
    
    
    
#while continue

i=0
while i<=5:
    i+=1
    if i==3:
        continue
    print(i)        
    