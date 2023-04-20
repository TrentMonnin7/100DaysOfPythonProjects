#prompts the to input the scores of the students in the class and splits by spaces
student_scores = input("Input a list of student scores ").split()
#assigns the current highest score to 0
highest_score=0

#For loop that iterates through the length of the list
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if (student_scores[n] > highest_score):
    highest_score = student_scores[n]

print(student_scores)
print(F"The highest score in the class is: {highest_score}")