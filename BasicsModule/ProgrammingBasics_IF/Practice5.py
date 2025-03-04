product = input()
day = input()
amount = float(input())

if (day == 'Monday'or
    day == 'Tuesday' or
    day == 'Wednesday' or
    day == 'Thursday' or
    day == 'Friday'):
    if product == 'banana':
        print(amount * 2.5)
    elif product == 'apple':
        print(amount * 1.2)
    elif product == 'orange':
        print(amount * 0.85)
    elif product == 'grapefruit':
        print(amount * 1.45)
    elif product == 'kiwi':
        print(amount * 2.7)
    elif product == 'pineapple':
        print(amount * 5.5)
    elif product == 'grapes':
        print(amount * 3.85)
elif day == 'Saturday' or day == 'Sunday':
    if product == 'banana':
        print(amount * 2.7)
    elif product == 'apple':
        print(amount * 1.25)
    elif product == 'orange':
        print(amount * 0.9)
    elif product == 'grapefruit':
        print(amount * 1.6)
    elif product == 'kiwi':
        print(amount * 3)
    elif product == 'pineapple':
        print(amount * 5.6)
    elif product == 'grapes':
        print(amount * 4.2)