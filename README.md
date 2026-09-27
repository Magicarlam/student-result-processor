Simple Student Result Processor

BIT223 – Week 2 Mini-Project

A procedural Python program that collects student information, calculates averages, classifies results, and processes multiple students using lists and dictionaries.

Features

- Stores a student's **name** and **registration number**.
- Accepts marks for three subjects.
- Uses `calculate_average()` to calculate the average.
- Uses `classify_result()` to classify the result.
- Uses a list of dictionaries to process many students.
- Validates marks so they remain between 0 and 100.
- Displays each student's final result.

Result Classification

| Average | Classification |
|---:|---|
| 70–100 | Distinction |
| 60–69.99 | Credit |
| 50–59.99 | Pass |
| Below 50 | Fail |

How to Run

Run the python file through terminal.

Then enter the number of students and their details when prompted.

Example

```text
===================================
   SIMPLE STUDENT RESULT PROCESSOR
===================================
Enter number of students: 1

Entering details for Student 1
Enter student name: Ryan Mugala
Enter registration number: 251203BSIT
Enter marks for three subjects:
Enter Subject 1 mark (0-100): 75
Enter Subject 2 mark (0-100): 68
Enter Subject 3 mark (0-100): 82

===================================
           ALL RESULTS
===================================

--- Student Result ---
Name: Ryan Mugala
Registration Number: 251203BSIT
Marks: [75.0, 68.0, 82.0]
Average: 75.00
Classification: Distinction

Processing complete.
```

Week 2 Procedural Concepts Demonstrated

- Variables
- Input and output
- Data types
- Lists
- Dictionaries
- Functions
- Conditional statements
- Loops
- Basic input validation

## Suggested Git Checkpoint

```bash
git innit
git add .
git commit -m "feat: complete Week 2 student result processor"
git status
```
