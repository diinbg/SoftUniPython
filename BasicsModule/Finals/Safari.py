budget = float(input())
fuel = float(input())
day = input()

sum = fuel * 2.1 + 100

if day == 'Saturday':
    sum = sum - sum * 0.1
elif day == 'Sunday':
    sum = sum - sum * 0.2

if sum <= budget:
    print(f'Safari time! Money left: {(budget - sum):.2f} lv.')
else:
    print(f'Not enough money! Money needed: {(sum - budget):.2f} lv.')