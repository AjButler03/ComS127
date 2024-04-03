# Andrew Butler             11-30-2022
# lab week 15 - exercise #1


# getting information from text files
def openfile(filename):
    with open(str(filename) + ".txt", "r") as students:
        lineslist = students.readlines()
        del lineslist[0]
        for i in range(0, len(lineslist)):
            lineslist[i] = lineslist[i].split(",")
            for j in range(0, len(lineslist[i])):
                lineslist[i][j] = lineslist[i][j].strip()
    return lineslist

studentsdata = openfile("students")
scoresdata = openfile("scores")

# combining gathered information into single list
master_grade_list = []
for student in studentsdata:
    master_grade_list.append(student)
    total_scores = 0
    sum_scores = 0
    avg_score = 0
    for grade in scoresdata:
        # Matching student ID to student ID listed on each score, combining data
        if grade[0] == student[0]:
            total_scores += 1
            sum_scores += int(grade[2])
    student.append(str(total_scores))
    student.append(str(sum_scores))
    student.append(str(sum_scores/total_scores))
master_grade_list.insert(0, ["Student ID", "Name", "Total Scores", "Sum of All Scores", "Score Average"])

# writing list into new file
with open("grades.txt", "w") as f:
    for i in range(0, len(master_grade_list)):
        for j in range(0, len(master_grade_list[i])):
            string = master_grade_list[i][j]
            if j < len(master_grade_list[i])-1:
                string += ","
            f.write(string)
        if i < len(master_grade_list)-1:
            f.write("\n")