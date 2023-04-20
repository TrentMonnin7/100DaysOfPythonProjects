#First way to do this
running_total=0
for num in range(0, 101, 2):
    running_total += num
print(running_total)


#Second way  to do this
running_total_2=0
for num in range(0,101):
    if  num  % 2 ==0:
        running_total_2 += num
print(running_total_2)