# Student Data Checker

A small Python project that checks a list of students for data problems. I made it because I check student records at work and wanted to practice automating that kind of check.

All the data is fake. `fake_students.py` makes 515 made-up students and puts mistakes in on purpose. No real student information is used.

## What it looks for
- missing emails, passport numbers, and dates
- emails that are not formatted right
- dates that do not exist (like Feb 30)
- passports that expire less than 6 months after the program starts
- students entered twice

## How to run
```
pip install pandas
python fake_students.py
python check_students.py
```
`check_students.py` prints a summary and saves every problem to `problems_found.csv`.

## Example output
```
rows checked: 515
students with a problem: 100
total problems: 106
```

## What I'd add next
- catch names that are almost the same (like "Jon" and "John")
- fix the easy problems automatically
- put the results in a chart
