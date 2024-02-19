# #for loop -break

# for i in range(5):
#     print(i)
#     break
# else:
#     print("finished")
    
# # #for loop -continue

# for i in range(5):
#     #continue (skip the itreation) #else -finished
#     print(i)
#     #break (Program terminates)
#     continue  #0-4 Finished
# else:
#     print("finished")

# # #2nd Case

# for i in range(5):
#     continue
#     print(i)
# else:
#     print("finished")
    
    
# for i in range(10):
#     pass #to write empty loop   it wont be executed itll be passed

# #work 

#even number within range 10-20
#even numbers sum within range 40-100
#Factorial(qn:7)
#Check number is prime or not(for loop qn:15)

#Nested for loop
#Pattern programming

#pattern 1

#*
#* *
#* * *
#* * * *
#* * * * *


# n=int(input("Enter the no of rows and clmn"))
#Outer loop
for i in range(4): #range(6) => i=0,1,2,3,4,5
    #inner loop
    for j in range(4-i): #j=0 (it wont print anything EX: '''print(list(range(0))''')
                        #j=1 range(1) =>1 time print
                        #j=2 range(1) =>2 time print
                        #j=3 range(1) =>3 time print
                        #j=4 range(1) =>4 time print
                        #j=5 range(1) =>5 time print
        print("*", end=" ")  #end =' ' used for empty spacing
    print()
    
    
    
    