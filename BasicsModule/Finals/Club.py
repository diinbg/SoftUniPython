profit = float(input())
sum = 0

while True:
    cocktail = input()

    if cocktail == 'Party!':
        print(f'We need {(profit - sum):.2f} leva more.')
        print(f'Club income - {sum:.2f} leva.')
        break

    cocktail_num = int(input())
    price = len(cocktail) * cocktail_num

    if price % 2 != 0:
        price = price - price * 0.25

    sum = sum + price

    if sum >= profit:
        print('Target acquired.')
        print(f'Club income - {sum:.2f} leva.')
        break
