subjects = ["Maths", "Science", "English", "History","Geography","Computer","Sanskrit"]
marks = {}
for subject in subjects:
    score = float(input(f"Enter marks for {subject}: "))
    marks[subject] = score
    
total = sum(marks.values())
average = total / len(subjects)
print("\n------ Marks Report ------")
print(f"{'Subject':<10} | {'Marks':<5}")
print("-" * 22)

for subject, score in marks.items():
    print(f"{subject:<10} | {score:<5.1f}")

print("-" * 22)
print(f"{'Total':<10} | {total:<5.1f}")
print(f"{'Average':<10} | {average:<5.2f}")