sumofmultiple =[]
num = 1
while num < 1000 : #range of numbers 
    if num % 3 == 0 or num % 5 == 0 :
        sumofmultiple.append(num)  #inputing all the number is an array
    num += 1

sumofmultiple
print('The multiple of 3 and 5 are: ' + str(sumofmultiple)) 

#Sum of the multiples
sum = 0

for i in sumofmultiple:
    sum = sum + i

print(sum)
