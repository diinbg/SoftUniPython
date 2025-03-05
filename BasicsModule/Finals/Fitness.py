clients = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for i in range(0, clients):
    activity = input()
    if activity == 'back':
        back += 1
    elif activity == 'chest':
        chest += 1
    elif activity == 'legs':
        legs += 1
    elif activity == 'abs':
        abs += 1
    elif activity == 'protein shake':
        protein_shake += 1
    elif activity == 'protein bar':
        protein_bar += 1

sum_protein = protein_shake + protein_bar
sum_workout = back + legs + chest + abs
training = sum_workout / clients * 100
protein = sum_protein / clients * 100

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{training:.2f}% - work out')
print(f'{protein:.2f}% - protein')