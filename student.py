student_ID =(int(input("enter your ID")))
print(student_ID)
student_Name =(input('enter your Name'))
print(student_Name)
student_age  =(int(input("enter your age")))
print(student_age)
quiz_score= float(input("enter marks quiz_score:"))
Assignment_score=float(input("enter marks Assignment_score:"))
exam_score= float(input("enter your exam_score:"))
student_attendance=int(input("enter your student_attendance"))
#arithmetic operator
total_score = quiz_score+ Assignment_score +exam_score+student_attendance
avg = total_score /4
#relational operator
is_passing =avg>75
#increment operator
student_attendance += 1
#logical operators
award= (student_attendance<=90)and (avg>75)

print("quiz_Score:", quiz_score)
print("Assignment_Score:", Assignment_score)
print("exam_Score:", exam_score)
print("student_attendance (after +1):", student_attendance)
print("Total Score:", total_score)
print("Average Score:", avg)

print("\n===== Status =====")
print("Passing Status:", is_passing)
print("Award :", award)

