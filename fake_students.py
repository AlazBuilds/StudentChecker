# makes a fake list of students with some mistakes put in on purpose
# none of this is real student data
import random
import pandas as pd

random.seed(1)

first_names = ["Maya", "Jordan", "Aiden", "Sofia", "Liam", "Zoe", "Noah", "Ava"]
last_names = ["Johnson", "Garcia", "Kim", "Patel", "Williams", "Brown", "Lopez"]
cities = ["Madrid", "London", "Paris", "Tokyo", "Sydney"]

rows = []
for i in range(1, 501):
    first = random.choice(first_names)
    last = random.choice(last_names)
    row = {}
    row["student_id"] = i
    row["first_name"] = first
    row["last_name"] = last
    row["email"] = first.lower() + "." + last.lower() + str(i) + "@example.com"
    row["birth_year"] = random.randint(2002, 2006)
    row["passport_number"] = "P" + str(random.randint(10000000, 99999999))
    row["passport_expires"] = str(random.randint(2028, 2034)) + "-06-01"
    row["program_city"] = random.choice(cities)
    row["program_start"] = "2027-" + str(random.randint(1, 8)).zfill(2) + "-15"
    rows.append(row)

df = pd.DataFrame(rows)

# put in some mistakes
# missing passport numbers
for i in random.sample(range(500), 25):
    df.loc[i, "passport_number"] = None

# missing emails
for i in random.sample(range(500), 18):
    df.loc[i, "email"] = None

# emails that are wrong
for i in random.sample(range(500), 20):
    df.loc[i, "email"] = "bademail.com"

# passport that expires too soon
for i in random.sample(range(500), 15):
    df.loc[i, "passport_expires"] = "2027-02-01"

# dates that dont exist
for i in random.sample(range(500), 10):
    df.loc[i, "passport_expires"] = "2030-02-30"

# same student twice
copies = df.sample(15, random_state=3).copy()
copies["student_id"] = range(501, 516)
df = pd.concat([df, copies])

df.to_csv("students.csv", index=False)
print("made students.csv with", len(df), "rows")
