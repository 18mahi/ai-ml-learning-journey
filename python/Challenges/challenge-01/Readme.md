# Student Grade Analyzer

A beginner-friendly Python project that analyzes student marks and generates a final grade report.

## Objective

Build a Python program that:

- Takes student details as input
- Accepts marks for 5 subjects
- Calculates total and percentage
- Assigns grades
- Checks pass/fail status
- Displays a clean report card

---

## Concepts Practiced

This challenge focuses on strengthening core Python fundamentals:

- `input()`
- `int()`
- Variables
- Arithmetic Operations
- `if-elif-else`
- Comparison Operators
- Logical Operators
- String Formatting
- Basic Program Logic

---

## Features

- Student Name Input
- Marks Entry for 5 Subjects
- Total Marks Calculation
- Percentage Calculation
- Grade Generation
- Pass/Fail Detection
- Clean Output Formatting

---

## Grade Criteria

|Percentage | Grade |
|-----------|-------|
| 90%+      | A+ |
| 80% - 89% | A |
| 70% - 79% | B |
| 60% - 69% | C |
| 50% - 59% | D |
| Below 50% | F |

---

## Pass Criteria

A student is considered **Pass** if:

- Percentage is **40% or above**
- No individual subject mark is below **33**

Otherwise:

```text
Status: Fail
```

---

## Sample Output

```text
Enter student name: Mahi

Enter marks for Subject 1: 85
Enter marks for Subject 2: 78
Enter marks for Subject 3: 92
Enter marks for Subject 4: 69
Enter marks for Subject 5: 88

------ Student Grade Report ------
Name: Mahi
Total Marks: 412 / 500
Percentage: 82.4%
Grade: A
Status: Pass
----------------------------------
```

---

## Bonus Improvements

Future improvements for this challenge:

- Use loops for input
- Store marks in a list
- Find highest marks
- Find lowest marks
- Calculate average marks
- Add multiple student support

---

## Learning Outcome

This project helps build strong fundamentals in **Python programming**, especially in **decision making, calculations, and program logic**, which are essential for moving toward **Data Science, AI/ML, and problem-solving**.
