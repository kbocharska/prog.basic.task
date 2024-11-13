import pickle
students_sorted = {}
with open("data.csv", "r") as datafile:
    next (datafile)
    for row in datafile:
        student = [int(i) if i.isdigit() else i for i in row[:-1].split(", ")]
        if student[3] not in students_sorted:
            students_sorted[student[3]] = {}
        if student[5] not in students_sorted[student[3]]:
            students_sorted[student[3]][student[5]] = [student]
        else:
            students_sorted[student[3]][student[5]].append(student)


with open('student_sorted.pkl', 'wb') as f:
    pickle.dump(students_sorted, f)

with open('student_sorted.pkl', 'rb') as f:
    students_sorted_loaded = pickle.load(f)
    for grade, prog_lang_list in students_sorted_loaded.items():
        print(grade)
        for prog_lang, students in prog_lang_list.items():
            print(f"  {prog_lang}: {students}")