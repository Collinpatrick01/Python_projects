#Changeing wegiht into pounds
weight= int(input('Weight: ')) #weight is in string 

unit = input('(L)bs or (K)g: ')# Type of weight Lbs -> pounds Kg -> kilogram

if unit.upper() == "L" :
      converted = weight * 0.45
      print(f" Your weight is {converted} pounds") #changing kilogram to pounds
elif unit.upper() == "K" : 
         converted = weight / 0.45 #converting pound to kilogram
         print(f"Your weight is {converted} kilogram")   
else:
      print('Enter Between "L" or " K " only')         
 


    
