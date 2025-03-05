easter_breads = int(input())
best_baker = ''
best_score = 0

for i in range(easter_breads):
    baker = input()
    score = 0
    while True:
        command = input()
        if command == 'Stop':
            print(f'{baker} has {score} points.')
            break

        score += int(command)

    if score > best_score:
        best_baker = baker
        best_score = score
        print(f'{baker} is the new number 1!')

print(f'{best_baker} won competition with {best_score} points!')