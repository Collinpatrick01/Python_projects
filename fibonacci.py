#Generating Fib number 
fibnum = [1, 2]

while fibnum[-1] <  4000000:
    fibnum.append( fibnum[-1] + fibnum[-2] )
del fibnum[-1] #deleting the number that exied 4M
#print(fibnum)      
       
# Sorting all the the even numberes
evenfibnumb = []
for i in fibnum:
   if i % 2 == 0:
       evenfibnumb.append(i)
print(evenfibnumb)
# Summing up all the even numberes on the Fib sequences

sums = 0

for sum in evenfibnumb:
    sums = sums + sum

print(sums)