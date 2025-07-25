#code for asking the user which operation he wants to perfrom for the given two numbers.
num_1 = float(input('enter number 1='))
num_2 = float(input('enter number 2='))

choice = input('enter your choice + _ = *')
if choice == '+':
    print(f'addition {num_1+num_2}')

elif choice == '-':
    print(f'subract{num_1-num_2}')


elif choice == '*':
     print(f'multiply{num_1*num_2}')


elif choice == '=':
    print(f'equal{num_1==num_2}')

else:
    print("invalid error")

 
#discount calculator
amount = float(input('enter the total amount:'))

discount = float(input('enter the discount for the amount 10 20 30'))
if discount == 10:
    print(f'{amount*discount/100}')
elif discount == 20:
    print(f'{amount*discount/100}')
elif discount == 30:
    print(f'{amount*discount/100}')
else:
    print('invalid discount')

orginal= float(input('enter the original amount:'))
discount= float(input('enter the amount after discount:'))
