import  math

name = input()
ep_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1/8
rest_time = break_duration * 1/4

free_time = break_duration - lunch_time - rest_time
time_left = math.ceil(ep_duration - free_time)

if ep_duration <= free_time:
    print("You have enough time to watch " + name + " and left with " + f"{time_left:.0f}" + " minutes of free time.")

elif ep_duration > free_time:
    print("You don't have enough time to watch " + name + ", you need " + f"{time_left:.0f}" + " more minutes.")