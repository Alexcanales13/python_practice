students = {
    "Ben": {"age": 12, "grade": 88, "favorite_subject": "Python"},
    "Alex": {"age": 13, "grade": 72, "favorite_subject": "Math"},
    "Mia": {"age": 12, "grade": 95, "favorite_subject": "Science"},
    "Noah": {"age": 14, "grade": 64, "favorite_subject": "Python"},
    "Emma": {"age": 13, "grade": 81, "favorite_subject": "Math"},
    "Liam": {"age": 12, "grade": 88, "favorite_subject": "Python"}
}


# --------------------------------------------------
# LEVEL 1: LOOK THROUGH A DICTIONARY
# --------------------------------------------------

print("\nCHALLENGE 1: Student Names")

for name in students:
    print(name)


print("\nCHALLENGE 2: Student Names and Grades")

for name, information in students.items():
    print(name, information["grade"])


print("\nCHALLENGE 3: Grades Above 80")

for name, information in students.items():
    if information["grade"] > 80:
        print(name)


print("\nCHALLENGE 4: Students Who Like Python")

for name, information in students.items():
    if information["favorite_subject"] == "Python":
        print(name)


print("\nCHALLENGE 5: Count Students")

count = 0

for name in students:
    count += 1

print("Total students:", count)


# --------------------------------------------------
# LEVEL 2: SEARCH FOR SPECIFIC INFORMATION
# --------------------------------------------------

print("\nCHALLENGE 6: Search by Subject")

subject = input("Enter a subject: ").strip().lower()
found = False

for name, information in students.items():
    if information["favorite_subject"].lower() == subject:
        print(name)
        found = True

if not found:
    print("No students found for that subject.")


print("\nCHALLENGE 7: Search for a Student")

search_name = input("Enter a student name: ").strip()
found = False

for name, information in students.items():
    if name.lower() == search_name.lower():
        print("Name:", name)
        print("Age:", information["age"])
        print("Grade:", information["grade"])
        print("Favorite subject:", information["favorite_subject"])
        found = True
        break

if not found:
    print("Student not found.")


print("\nCHALLENGE 8: Highest Grade")

highest_name = None
highest_grade = None

for name, information in students.items():
    grade = information["grade"]

    if highest_grade is None or grade > highest_grade:
        highest_grade = grade
        highest_name = name

print("Highest-scoring student:", highest_name)
print("Grade:", highest_grade)


print("\nCHALLENGE 9: Lowest Grade")

lowest_name = None
lowest_grade = None

for name, information in students.items():
    grade = information["grade"]

    if lowest_grade is None or grade < lowest_grade:
        lowest_grade = grade
        lowest_name = name

print("Lowest-scoring student:", lowest_name)
print("Grade:", lowest_grade)


print("\nCHALLENGE 10: Count Passing Students")

count = 0

for name, information in students.items():
    if information["grade"] >= 80:
        count += 1

print("Students with grades of 80 or higher:", count)


# --------------------------------------------------
# LEVEL 3: BUILD A NEW DICTIONARY
# --------------------------------------------------

print("\nCHALLENGE 11: Passing Students")

passing_students = {}

for name, information in students.items():
    if information["grade"] >= 70:
        passing_students[name] = information

print(passing_students)


print("\nCHALLENGE 12: Python Students")

python_students = {}

for name, information in students.items():
    if information["favorite_subject"] == "Python":
        python_students[name] = information

print(python_students)


print("\nCHALLENGE 13: Students Aged 12")

twelve_year_old_students = {}

for name, information in students.items():
    if information["age"] == 12:
        twelve_year_old_students[name] = information

print(twelve_year_old_students)


print("\nCHALLENGE 14: Grades of 85 or Higher")

high_scorers = {}

for name, information in students.items():
    if information["grade"] >= 85:
        high_scorers[name] = information

print(high_scorers)


print("\nCHALLENGE 15: Filter by Minimum Grade")

minimum_grade = int(input("Enter a minimum grade: "))
filtered_students = {}

for name, information in students.items():
    if information["grade"] >= minimum_grade:
        filtered_students[name] = information

print(filtered_students)


# --------------------------------------------------
# LEVEL 4: PARSE NESTED DICTIONARIES
# --------------------------------------------------

print("\nCHALLENGE 16: Complete Student Records")

for name, information in students.items():
    print("--------------------")
    print("Name:", name)
    print("Age:", information["age"])
    print("Grade:", information["grade"])
    print("Favorite subject:", information["favorite_subject"])


print("\nCHALLENGE 17: Students Matching Both Conditions")

for name, information in students.items():
    if information["age"] >= 13 and information["grade"] > 75:
        print(name, information)


print("\nCHALLENGE 18: Count Students by Subject")

subject_counts = {}

for name, information in students.items():
    subject = information["favorite_subject"]

    if subject not in subject_counts:
        subject_counts[subject] = 0

    subject_counts[subject] += 1

print(subject_counts)


print("\nCHALLENGE 19: Students With the Same Grade")

student_names = list(students.keys())

for i in range(len(student_names)):
    name1 = student_names[i]
    grade1 = students[name1]["grade"]

    for j in range(i + 1, len(student_names)):
        name2 = student_names[j]
        grade2 = students[name2]["grade"]

        if grade1 == grade2:
            print(name1, "and", name2, "both scored", grade1)


print("\nCHALLENGE 20: Class Average")

total = 0
count = 0

for name, information in students.items():
    total += information["grade"]
    count += 1

if count > 0:
    average = total / count
    print("Class average:", round(average, 2))
else:
    print("There are no students.")


# --------------------------------------------------
# LEVEL 5: MORE CHALLENGING
# --------------------------------------------------

print("\nCHALLENGE 21: Most Popular Subject")

subject_counts = {}

for name, information in students.items():
    subject = information["favorite_subject"]

    if subject not in subject_counts:
        subject_counts[subject] = 0

    subject_counts[subject] += 1

most_popular_subject = None
highest_count = 0

for subject, count in subject_counts.items():
    if count > highest_count:
        highest_count = count
        most_popular_subject = subject

print("Most popular subject:", most_popular_subject)
print("Number of students:", highest_count)


print("\nCHALLENGE 22: Students Above the Class Average")

total = 0
count = 0

for name, information in students.items():
    total += information["grade"]
    count += 1

average = total / count

print("Class average:", round(average, 2))

for name, information in students.items():
    if information["grade"] > average:
        print(name, information["grade"])


print("\nCHALLENGE 23: Average Grade by Subject")

search_subject = input("Enter a subject: ").strip().lower()

total = 0
count = 0

for name, information in students.items():
    if information["favorite_subject"].lower() == search_subject:
        total += information["grade"]
        count += 1

if count > 0:
    average = total / count
    print("Average grade for", search_subject, ":", round(average, 2))
else:
    print("No students found for that subject.")


print("\nCHALLENGE 24: Group Students by Subject")

students_by_subject = {}

for name, information in students.items():
    subject = information["favorite_subject"]

    if subject not in students_by_subject:
        students_by_subject[subject] = []

    students_by_subject[subject].append(name)

print(students_by_subject)


# --------------------------------------------------
# FINAL CHALLENGE: STUDENT REPORT
# --------------------------------------------------

def show_student_grades():
    print("\n--- Student Grades ---")

    for name, information in students.items():
        print(name, ":", information["grade"])


def calculate_class_average():
    total = 0
    count = 0

    for name, information in students.items():
        total += information["grade"]
        count += 1

    if count == 0:
        return 0

    return total / count


def find_highest_student():
    highest_name = None
    highest_grade = None

    for name, information in students.items():
        grade = information["grade"]

        if highest_grade is None or grade > highest_grade:
            highest_name = name
            highest_grade = grade

    if highest_name is not None:
        print("Highest:", highest_name, "-", highest_grade)


def find_lowest_student():
    lowest_name = None
    lowest_grade = None

    for name, information in students.items():
        grade = information["grade"]

        if lowest_grade is None or grade < lowest_grade:
            lowest_name = name
            lowest_grade = grade

    if lowest_name is not None:
        print("Lowest:", lowest_name, "-", lowest_grade)


def show_passing_students():
    print("\n--- Passing Students ---")

    for name, information in students.items():
        if information["grade"] >= 70:
            print(name, information["grade"])


def show_subject_counts():
    print("\n--- Students by Subject ---")

    subject_counts = {}

    for name, information in students.items():
        subject = information["favorite_subject"]

        if subject not in subject_counts:
            subject_counts[subject] = 0

        subject_counts[subject] += 1

    for subject, count in subject_counts.items():
        print(subject, ":", count)


def show_above_average_students():
    print("\n--- Above-Average Students ---")

    average = calculate_class_average()

    for name, information in students.items():
        if information["grade"] > average:
            print(name, information["grade"])


def generate_report():
    print("\n==============================")
    print("       STUDENT REPORT")
    print("==============================")

    show_student_grades()

    average = calculate_class_average()
    print("\nClass average:", round(average, 2))

    find_highest_student()
    find_lowest_student()
    show_passing_students()
    show_subject_counts()
    show_above_average_students()


generate_report()