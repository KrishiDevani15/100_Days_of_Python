student_scores = [180, 124, 165, 173, 189, 169, 146]
#1) One way to get the total score
total_exam_score = sum(student_scores)

#2) Second way to get the total score using loops
total_sum = 0
for score in student_scores:
    total_sum +=score

# 3) Calculate the mAx score
print(max(student_scores))

# 4) Calculate the max score using loops
max_score = None
for score in student_scores:
    if max_score is None or score > max_score:
        max_score = score

print(max_score)