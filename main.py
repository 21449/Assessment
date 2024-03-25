def instructions():
    print('\n')

totalpayed = 0
totalprofit = 0
for x in range(4):

    ins = input("\n\nwould you like to see the instructions? \n").lower()

    if ins in ('y', 'yes', 'yeah', 'yep'):
        instructions()

    elif ins in ('n', 'no', 'nah'):
        print()


    name = '1'
    agevalid = False

    while agevalid == False:
        name = '1'

        while not name.isalpha():
            name = input('what is the ticket holders name? \n')

            if name.isalpha():
                print()
            else:
                print('please enter a valid name\n')

        age = 'a'
        while not age.isnumeric():
            age = input(f'how old are you {name}? ')

            if not age.isnumeric():
                print('please enter a valid age\n')
            
            elif age.isnumeric():
                age1 = int(age)

        if age1 <= 11:
            print('sorry your not old enough\n\n\n')
        
        else:
            agevalid = True

    if age1 < 16:
        cost = 7.50
        profit = 2.50

    elif age1 >= 65:
        cost = 6.50
        profit = 1.50

    else:
        cost = 10.50
        profit = 5.50
    
    totalpayed = totalpayed + cost
    totalprofit = totalprofit + profit

    print(f"{totalprofit}, {totalpayed}")

    payment = input('please enter "cash" or "card"\n').lower()
    
    while payment not in ('cash', 'card'):
        payment = input('please enter "cash" or "card"\n').lower()

    if payment == 'card':
        
        surcharge = cost * 0.05
        total = surcharge + cost
        
        print(f'\nthat will be ${total:.2f}')
        

    elif payment == "cash":
        print(f'\nthat will be ${cost:.2f}')

print(f"\n\nyou earned a total of ${totalpayed} and that is ${totalprofit} of profit")