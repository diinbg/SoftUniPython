n = int(input())
salary = float(input())

for i in range(0, n):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50

if salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{salary:.0f}')