time1 = int(input())
time2 = int(input())
time3 = int(input())

sum = time3 + time2 + time1

minutes = sum // 60
seconds = sum % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')