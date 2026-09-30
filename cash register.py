#Cash Register 
#Vilina Prenko
#26.08.2025 - total, payment, change and breakdown

total = int(float(input('Total amount: '))*100)
payment = int(float(input('How much are you paying? '))*100)

money = total % payment

change = payment - total

#bills
bills100 = change//10000
change = change % 10000

bills50 = change//5000
change = change % 5000

bills20 = change//2000
change = change % 2000

bills10 = change//1000
change = change % 1000

bills5 = change//500
change = change % 500

bills1 = change//100
change = change % 100

cents25 = change//25
change = change % 25

cents10 = change//10
change = change % 10 

cents5 = change//5
cents5 = change % 5

cents = change


if money < 1:
    print('More money!')
else: 
   print(f'Your change: ${(change/100):.f2}')
   print (f'Your breakdown: /n $100: {bills100} /n $50: {bills50} /n $20: {bills20} /n $10: {bills10} /n $5: {bills5} /n')


