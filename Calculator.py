# Calculator

a = int(input("Enter first number: "))

print("Choose number of an operator ....")
print("1: +, " " 2: -, " "3: /, " "4: *, " "5: %  " " and " "6: **" )
num = int(input())
# c = int(input())  input variable 
b = int(input("Enter second number: "))
opt = num
if opt == 1:
    print (a + b)
elif opt == 2 :
    print(a - b)
elif opt == 3 :
    print(a / b) 
elif opt == 4 :
    print(a * b)
elif opt == 5 :
    print(a % b)
elif opt == 6 :
    print(a ** b)
else :
    print("Syntax error") 
