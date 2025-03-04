inpt = input()
sum = 0.0

while inpt != 'NoMoreMoney':
    amount = float(inpt)
    if amount < 0:
        print('Invalid operation!')

    sum += amount
    print(f'Increase: {amount:.2f}')
    inpt = input()

print(f'Total: {sum:.2f}')