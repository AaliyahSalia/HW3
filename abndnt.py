def abndnt(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum > n

n = int(input("Please enter a number: "))
print(abndnt(n))
    
