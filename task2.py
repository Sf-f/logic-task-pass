#Q2/Write a program to find all prime numbers up to a given range of numbers?


x=50
y=100

print("prime numbers between {} and {} :" .format(x,y))

for num in range(x, y+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
           print(num)


