#finding max score in students_score

student_score = [20,233,35,6,4,4623,2423,23,233,65,623,2,523,346,6,45,47,34,2,34,34,634,6,346,34646,34,634,264,32,4,2,322]

max_score = 0
for score in student_score:
    if score> max_score:
        max_score = score

print(max_score)