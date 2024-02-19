#Pattern prgramming


#upside down
#49
#  * * * *    
#  * * *
#  * *
#  *

n=int(input("Enter the number of column and rows"))
for i in range (n):
    for j in range (n-i):
        print("*",end="")
    for k in range (n):
        print(" ", end="")
    print()


#upside down 
#50

# * * * *
#   * * *
#     * * 
#       *

n=int(input("Enter the number of column and rows"))
for i in range (n):
    for j in range (i):
        print(" ",end="")
    for k in range (n-i):
        print("*", end="")
    print()




#51

#       *
#     * * *
#   * * * * *
# * * * * * * *



n=int(input("Enter the number of column and rows"))
for i in range (n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range(2*i+1):
        print("*" , end="")
    print()


#upside down

# * * * * * * *
#   * * * * *
#     * * *
#       *

n=int(input("Enter the number of column and rows"))
for i in range (n):
    for j in range(i):
        print(" ", end="")
    for k in range(n+3-2*i):
        print("*" , end="")
    print()

    

