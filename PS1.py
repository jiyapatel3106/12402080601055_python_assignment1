def main():
n, k, m = map(int, input().split()) if not (1 <= n <= 100000):
raise ValueError("Number of students must be between 1 and 100000.")

if not (1 <= k <= 50):
raise ValueError("K must be between 1 and 50.")

if not (1 <= m <= 12):
raise ValueError("Number of subjects must be between 1 and 12.") semester_students = {}
subject_toppers = {} for i in range(1, m + 1):
subject_toppers[f"S{i}"] = (-1, [])
for _ in range(n):
data = input().split()

enrollment = data[0] name = data[1] semester = int(data[2]) cpi = float(data[3])
marks = list(map(int, data[4:])) if len(marks) != m:
raise ValueError(
f"{enrollment} must have exactly {m} subject marks."
)

if any(mark < 0 or mark > 100 for mark in marks):
raise ValueError("Marks must be between 0 and 100.")
 
if not (1 <= semester <= 8):
raise ValueError("Semester must be between 1 and 8.")

if not (0.0 <= cpi <= 10.0):
raise ValueError("CPI must be between 0.0 and 10.0.") average_marks = sum(marks) / m
student = ( enrollment, name,
cpi, average_marks, marks
)
if semester not in semester_students: semester_students[semester] = []
semester_students[semester].append(student
) for i, mark in enumerate(marks, start=1): subject = f"S{i}"
highest_mark, toppers = subject_toppers[subject] if mark > highest_mark:
subject_toppers[subject] = (mark, [enrollment])
elif mark == highest_mark: toppers.append(enrollment)
for	semester	in sorted(semester_students): students = semester_students[semester] students.sort(
key=lambda student: (
-student[2],
-student[3], student[0]
)
)
top_students = students[:k]
 

enrollments = [student[0] for student in top_students] print(f"Semester {semester}:", *enrollments)
for i in range(1, m + 1): subject = f"S{i}"
highest_mark, toppers = subject_toppers[subject] toppers.sort()
print(f"{subject}:",
*toppers) if  name == " main ": main()
