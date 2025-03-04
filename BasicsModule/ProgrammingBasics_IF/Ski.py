days_stayed = int(input())
room_type = input()
rating = input()

price = 0
nights = days_stayed - 1

if room_type == 'room for one person':
    price = nights * 18
elif room_type == 'apartment':
    price = nights * 25
    if days_stayed < 10:
        price = price - price * 0.3
    elif 10 <= days_stayed <= 15:
        price = price - price * 0.35
    elif days_stayed > 15:
        price = price - price * 0.50
elif room_type == 'president apartment':
    price = nights * 35
    if days_stayed < 10:
        price = price - price * 0.1
    elif 10 <= days_stayed <= 15:
        price = price - price * 0.15
    elif days_stayed > 15:
        price = price - price * 0.2

if rating == 'positive':
    price = price + price * 0.25
elif rating == 'negative':
    price = price - price * 0.1

print(f'{price:.2f}')