import math
from symbol import factor

# Inputing the number
num =int(input("Enter number to find it's Prime number: "))
#LIst to store you prime factors
prime_num = []
#Sorting Prime factors
while num % 2 == 0:
    prime_num.append(2)
    num //=2

divisor = 3
while num != 1 and divisor <= num :
    if num % divisor == 0:
        prime_num.append(divisor)
        num //= divisor
    else:
        divisor += 2
prime_num

print("The prime factor are:" + str(prime_num))



# for i in range(len(prime_num)):
#     print(prime_num[i], end='')
     

#Finding the largest Prime factor
