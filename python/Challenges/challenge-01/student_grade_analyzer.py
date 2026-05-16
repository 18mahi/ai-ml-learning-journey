## Ask for student name ##
stu=input("Enter student name : ")

## ask for marks in 5 subjects ##

total_marks = 0
has_failed_subject = False
for i in range(1,6):
  mark_input = input(f"Enter marks for Subject {i}: ")
  total_marks = total_marks + int(mark_input)
  if(int((mark_input)))<33:
    has_failed_subject = True
    
## percentage ##
percentage = (total_marks / 500) * 100

## grade ##

if(percentage>=90):
  Grade= "A+"
elif(percentage>=80 and percentage<=89):
  Grade= "A"
elif(percentage>=70 and percentage<=79):
  Grade= "B"
elif(percentage>=60 and percentage<=69):
  Grade= "C"
elif(percentage>=50 and percentage<=59):
  Grade="D"
else:
  Grade= "F"
  
## pass rule #
if(percentage>=40 and has_failed_subject == False):
    Status="Pass"
else:
  Status="Fail"

## final report ##

print("\n------ Student Grade Report ------")
print(f"Name: {stu}")
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {Grade}")
print(f"Status: {Status}")
print("----------------------------------")

### Bonus task ###
import statistics as math
marks=[]
for i in range(1,6):
  marks.append(int(input(f"enter marks of subject {i}: ")))
print("highest marks: ",max(marks))
print("lowest marks: ",min(marks))
print("average marks: ",math.mean(marks))
