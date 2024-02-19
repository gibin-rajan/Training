#Pattern programming


#       *
#     * *
#   * * *
# * * * *


# space           star         i-value
# 3                 1             0
# 2                 2             1
# 1                 3             2
# 0                 4             3

from pkg_resources import WorkingSet


n=int(input("Enter the number of column and rows"))
#outerloop
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
    
    
# Work

# 19qns
#Fibonacci series



# 22qns
#Prime number upto a given limit

