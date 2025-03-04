import math

people = int(input())
entry = float(input())
chair = float(input())
umbrella = float(input())

sum = people * entry + math.ceil(people * 0.75) * chair + math.ceil(people * 0.5) * umbrella

print(f"{sum:.2f} lv.")