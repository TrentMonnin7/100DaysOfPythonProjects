student_heights = input("Input a list of student heights ").split()
sum_of_heights = 0
running_loop_total  = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_of_heights += student_heights[n]
  running_loop_total += 1

average = round(sum_of_heights/running_loop_total)

print(average)