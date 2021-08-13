#ATM

# Pooja would like to withdraw X $US from an ATM.
# The cash machine will only accept the transaction if X is a multiple of 5,
# and Pooja's account balance has enough cash to perform the withdrawal 
# transaction (including bank charges). 
# For each successful withdrawal the bank charges 0.50 $US. 
# Calculate Pooja's account balance after an attempted transaction. 

# Input

# Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to 
# withdraw.

# Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's 
# initial account balance. 

# Output

# Output the account balance after the attempted transaction, 
# given as a number with two digits of precision. 
# If there is not enough money in the account to complete the transaction, 
# output the current bank balance. 

# Example - Successful Transaction

# Input:
# 30 120.00

# Output:
# 89.50

# Example - Incorrect Withdrawal Amount (not multiple of 5)

# Input:
# 42 120.00

# Output:
# 120.00

# Example - Insufficient Funds

# Input:
# 300 120.00

# Output:
# 120.00


#Amount withdraw Pooja Account  balance  initial

amount_withdraw, amount_balance= map(float,  input().split())
#ATM Withdraw criteria ie X % 5 == 0
if amount_withdraw % 5 ==0 and amount_withdraw + 0.50 <= amount_balance :
   #Bank charges 0.50
   new_balance = amount_balance - amount_withdraw - 0.50
   print("%.2f"%new_balance)  #"%.2f"% two decimal places
else:
    print("%.2f"%amount_balance)


      #   withdrawal_amount,balance = map(float, input().split())
      #   if withdrawal_amount +0.50 <= balance and int(withdrawal_amount) % 5 == 0:
      #       current_balance = balance - withdrawal_amount - 0.50
      #       print("%.2f"%current_balance)
      #   else:
      #       print("%.2f"%balance)