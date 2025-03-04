city = input()
package = input()
vip = input()
days = int(input())
sum = 0

if 7 >= days >= 1:
    if city == 'Bansko' or city == 'Borovets':
        if package == 'noEquipment':
            if vip == 'yes':
                sum = days * 80 - days * 80 * 0.05
                print(f'The price is {sum:.2f}lv! Have a nice time')
            elif vip == 'no':
                sum = days * 80
                print(f'The price is {sum:.2f}lv! Have a nice time')
        elif package == 'withEquipment':
            if vip == 'yes':
                sum = days * 100 - days * 100 * 0.1
                print(f'The price is {sum:.2f}lv! Have a nice time')
            elif vip == 'no':
                sum = days * 100
                print(f'The price is {sum:.2f}lv! Have a nice time')
        else:
            print('Invalid input!')
    elif city == 'Varna' or city == 'Burgas':
        if package == 'noBreakfast':
            if vip == 'yes':
                sum = days * 100 - days * 100 * 0.07
                print(f'The price is {sum:.2f}lv! Have a nice time')
            elif vip == 'no':
                sum = days * 100
                print(f'The price is {sum:.2f}lv! Have a nice time')
        elif package == 'withBreakfast':
            if vip == 'yes':
                sum = days * 130 - days * 130 * 0.12
                print(f'The price is {sum:.2f}lv! Have a nice time')
            elif vip == 'no':
                sum = days * 130
                print(f'The price is {sum:.2f}lv! Have a nice time')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
elif days > 7:
    days -= 1
    if city == 'Bansko' or city == 'Borovets':
        if package == 'noEquipment':
            if vip == 'yes':
                sum = days * 80 - days * 80 * 0.05
                print(f'The price is {sum:.2f}lv! Have a nice time')
            elif vip == 'no':
                sum = days * 80
                print(f'The price is {sum:.2f}lv! Have a nice time')
        elif package == 'withEquipment':
            if vip == 'yes':
                sum = days * 100 - days * 100 * 0.1
                print(f'The price is {sum:.2f}lv! Have a nice time')
            elif vip == 'no':
                sum = days * 100
                print(f'The price is {sum:.2f}lv! Have a nice time')
        else:
            print('Invalid input!')
    elif city == 'Varna' or city == 'Burgas':
        if package == 'noBreakfast':
            if vip == 'yes':
                sum = days * 100 - days * 100 * 0.07
                print(f'The price is {sum:.2f}lv! Have a nice time')
            elif vip == 'no':
                sum = days * 80
                print(f'The price is {sum:.2f}lv! Have a nice time')
        elif package == 'withBreakfast':
            if vip == 'yes':
                sum = days * 130 - days * 130 * 0.12
                print(f'The price is {sum:.2f}lv! Have a nice time')
            elif vip == 'no':
                sum = days * 130
                print(f'The price is {sum:.2f}lv! Have a nice time')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
elif days < 1:
    print('Days must be positive number!')
