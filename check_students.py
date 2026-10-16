# reads students.csv and finds the problems in it
import pandas as pd

df = pd.read_csv("students.csv", dtype=str)
df = df.reset_index(drop=True)

problems = []  # each problem gets added here

# 1. missing values
for col in ["email", "passport_number", "passport_expires", "birth_year"]:
    for i in range(len(df)):
        if pd.isna(df.loc[i, col]):
            problems.append([df.loc[i, "student_id"], "missing " + col])

# 2. bad emails (needs an @ and a . after it)
for i in range(len(df)):
    email = df.loc[i, "email"]
    if pd.isna(email):
        continue
    if "@" not in email or "." not in email.split("@")[-1]:
        problems.append([df.loc[i, "student_id"], "bad email"])

# 3. dates that are not real dates
for i in range(len(df)):
    d = df.loc[i, "passport_expires"]
    if pd.isna(d):
        continue
    try:
        pd.to_datetime(d, format="%Y-%m-%d")
    except ValueError:
        problems.append([df.loc[i, "student_id"], "date doesnt exist"])

# 4. passport runs out less than 6 months after the program starts
for i in range(len(df)):
    try:
        start = pd.to_datetime(df.loc[i, "program_start"])
        end = pd.to_datetime(df.loc[i, "passport_expires"])
    except ValueError:
        continue
    if pd.isna(start) or pd.isna(end):
        continue
    if end < start + pd.DateOffset(months=6):
        problems.append([df.loc[i, "student_id"], "passport expires too soon"])

# 5. duplicates (same name, birth year and passport)
dupes = df[df.duplicated(subset=["first_name", "last_name", "birth_year", "passport_number"])]
for i in dupes.index:
    if not pd.isna(df.loc[i, "passport_number"]):
        problems.append([df.loc[i, "student_id"], "duplicate"])

result = pd.DataFrame(problems, columns=["student_id", "problem"])
result.to_csv("problems_found.csv", index=False)

print("rows checked:", len(df))
print("students with a problem:", result["student_id"].nunique())
print("total problems:", len(result))
print()
print(result["problem"].value_counts())
