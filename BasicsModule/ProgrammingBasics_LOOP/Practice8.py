import sys

n = int(input())
smallest = sys.maxsize
biggest = -sys.maxsize

for i in range(0, n):
    num = int(input())
    if num < smallest:
        smallest = num
    elif num > biggest:
        biggest = num

print('Max number: ', biggest)
print('Min number: ', smallest)