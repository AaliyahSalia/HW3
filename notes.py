for count in range(1, 11):
        multi = num * count
        print(num, 'x', count, '=', multi)


        for i in range(1, 11)):
        print(i)

    for count in range(num):
        multi = count * num
        print(multi)


Write a function to take a positive integer x as input and print all 
ways of forming positive integer x by multiplying 
two positive integers together, ordered by the first 
term. Then, return whether the sum of the proper divisors of 
x is greater than x. 
def abndnt(n):
   """
   >>> abndnt(12) # 1 + 2 + 3 + 4 + 6 is 16, which is larger than 12 
   1 * 12 
   2 * 6 
   3 * 4 
   True 
  >>> abndnt (14)  # 1 + 2 + 7 is 10, which is not larger than 14 
   1 * 14 
   2 * 7 
   False 
   >>> abndnt (16) 

   def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n
print(is_abundant(12))
print(is_abundant(13))

n = 12

sum=1 # 1 can divide any number 

for i in range(2,n):
  if(n%i==0):    #if number is divisible by i add the number 
   sum=sum+i

if(sum>n):
  print(n,'is Abundant Number')

else:
  print(n,'is not Abundant Number')