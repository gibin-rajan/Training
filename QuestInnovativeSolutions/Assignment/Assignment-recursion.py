# factorial of given number
def factorial(n):
	if (n==1 or n==0):
		return 1
	else:
		return (n * factorial(n - 1))
num=int(input("Enter the number"))
print("Factorial : ",factorial(num))


#  Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

x = int(input("Enter the number"))
if x <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(x):
       print(recur_fibo(i))