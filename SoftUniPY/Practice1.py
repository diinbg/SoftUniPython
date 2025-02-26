product = input()
city = input()
amount = float(input())

if city == 'Sofia':
    if product == 'coffee':
        price = amount * 0.5
        print(f'{price:.1f}')
    elif product == 'water':
        price = amount * 0.8
        print(f'{price:.1f}')
    elif product == 'beer':
        price = amount * 1.2
        print(f'{price:.1f}')
    elif product == 'sweets':
        price = amount * 1.45
        print(f'{price:.1f}')
    elif product == 'peanuts':
        price = amount * 1.6
        print(f'{price:.1f}')
elif city == 'Plovdiv':
    if product == 'coffee':
        price = amount * 0.4
        print(f'{price:.1f}')
    elif product == 'water':
        price = amount * 0.7
        print(f'{price:.1f}')
    elif product == 'beer':
        price = amount * 1.15
        print(f'{price:.1f}')
    elif product == 'sweets':
        price = amount * 1.30
        print(f'{price:.1f}')
    elif product == 'peanuts':
        price = amount * 1.5
        print(f'{price:.1f}')
elif city == 'Varna':
    if product == 'coffee':
        price = amount * 0.45
        print(f'{price:.1f}')
    elif product == 'water':
        price = amount * 0.7
        print(f'{price:.1f}')
    elif product == 'beer':
        price = amount * 1.1
        print(f'{price:.1f}')
    elif product == 'sweets':
        price = amount * 1.35
        print(f'{price:.1f}')
    elif product == 'peanuts':
        price = amount * 1.55
        print(f'{price:.1f}')