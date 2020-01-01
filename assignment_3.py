import math
import matplotlib.pyplot as plt
import datasheet as dt

student_attendence_set = [
    { "name": "Waasay Anwar", "id": "1130715", "attendance": 
        [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1], 
        "percentage": 0, "marks": 0 },

    { "name": "Sumon Ahmad", "id": "1310173", "attendance": 
        [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        "percentage": 0, "marks": 0 },
    
    { "name": "Abdullah All Rakib", "id": "1420443", "attendance": 
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        "percentage": 0, "marks": 0 },

    { "name": "Md. Zillur Rahman", "id": "1510157", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1], 
        "percentage": 0, "marks": 0 },

    { "name": "Kazi Sabbir Anwar", "id": "1511242", "attendance": 
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
        "percentage": 0, "marks": 0 },
    
    { "name": "Sumaiya Habib Poushy", "id": "1511466", "attendance": 
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
        "percentage": 0, "marks": 0 },

    { "name": "Ezab Quader", "id": "1512081", "attendance": 
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1], 
        "percentage": 0, "marks": 0 },

    { "name": "S.M Nasif Sadiq", "id": "1530117", "attendance": 
        [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0], 
        "percentage": 0, "marks": 0 },

    { "name": "Sadia Afroz", "id": "1530140", "attendance": 
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        "percentage": 0, "marks": 0 },

    { "name": "Razib Sikder", "id": "1530852", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], 
        "percentage": 0, "marks": 0 },

    { "name": "Abdullah Al Mamun", "id": "1530117", "attendance": 
        [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1], 
        "percentage": 0, "marks": 0 },

    { "name": "Md. Rakib Imtiaz", "id": "1610294", "attendance": 
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], 
        "percentage": 0, "marks": 0 },

    { "name": "Inkiad Md. Abrar", "id": "1610596", "attendance": 
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0], 
        "percentage": 0, "marks": 0 },
    
    { "name": "Md. Adib Shahriar", "id": "1610834", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Durjoy Dass", "id": "1610834", "attendance": 
        [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Ucchawas", "id": "1620016", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },

    { "name": "S.M. Iftikhar Rasha", "id": "1620221", "attendance": 
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        "percentage": 0, "marks": 0 },
    
    { "name": "Marufa Tasnim", "id": "1620287", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },
    
    { "name": "Moshedul Bari Antor", "id": "1620345", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Md. Raian Hossain", "id": "1620363", "attendance": 
        [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
        "percentage": 0, "marks": 0 },

    { "name": "Assadujjaman Nayeem", "id": "1620538", "attendance": 
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Md. Golam Shakir", "id": "1620198", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Md. Yeasir Hossain", "id": "1620601", "attendance": 
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Ankur Saha", "id": "1620753", "attendance": 
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Shazid Hasan Riam", "id": "1621060", "attendance": 
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
        "percentage": 0, "marks": 0 },

    { "name": "Tahrim Faroque Tushar", "id": "1621148", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Maliha Mamtaz", "id": "1621418", "attendance": 
        [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
        "percentage": 0, "marks": 0 },

    { "name": "Nadim Mahmud Dipu", "id": "1711097", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },
    
    { "name": "Sifatul Alam Shohan", "id": "1711385", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Refat Chowdhury", "id": "1711443", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "percentage": 0, "marks": 0 },

    { "name": "Mushfiqur Rahman", "id": "1711552", "attendance": 
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        "percentage": 0, "marks": 0 }  
]
class_taken = 16

attendance_count = { "70": 0, "60": 0, "45": 0, "30": 0 }

for student_attendence in student_attendence_set:
    count = sum(student_attendence["attendance"])
    student_attendence["percentage"] = math.ceil(count * 100 / class_taken)

for student_attendence in student_attendence_set:
    
    if student_attendence["percentage"] >= 70:
        student_attendence["marks"] = 5
    
    elif student_attendence["percentage"] >= 60:
        student_attendence["marks"] = 4
    
    elif student_attendence["percentage"] >= 45:
        student_attendence["marks"] = 3
    
    elif student_attendence["percentage"] >= 30:
        student_attendence["marks"] = 2

print("Calculated Attendance Percentage")
print("No.\t\tName\t\tID\t\t\tPercentage\t\tMarks")

count = 1

for student_attendence in student_attendence_set:
    print("{}{}{}\t\t\t{}\t\t{}".format(count, student_attendence["name"].rjust(24), student_attendence["id"].rjust(20), student_attendence["percentage"], student_attendence["marks"]))
    count = count + 1


    
for student_attendence in student_attendence_set:

    if student_attendence["percentage"] >= 70:
        attendance_count["70"] += 1
    
    elif student_attendence["percentage"] >= 60:
        attendance_count["60"] += 1
    
    elif student_attendence["percentage"] >= 45:
        attendance_count["45"] += 1
    
    elif student_attendence["percentage"] >= 30:
        attendance_count["30"] += 1

print("Attendance Percentage (Student Count)")
print("No.\tPercentage\tCount")

count = 1

for student_attendence in attendance_count.keys():
    print("{}\t{}\t{}\t".format(count, student_attendence, attendance_count[student_attendence]))
    count = count + 1


labels = "70%", "60%", "45%", "30%"
sizes = [attendance_count["70"], attendance_count["60"], attendance_count["45"], attendance_count["30"]]
colors = ['#008fd5', '#dc4f38' , '#e5ae37', '#19ff19']

#ax1 = plt.subplots()
plt.pie(sizes, labels = labels, colors=colors,wedgeprops={'edgecolor':'black'}, autopct="%1.1f%%", startangle = 90)
plt.axis("equal")
plt.title("Attendance Percentage Student Count")
plt.tight_layout()

plt.show()

def show_barChart():
    
    id_list = []
    
    for student_attendence in student_attendence_set:
        id_list.append(student_attendence["id"][0:3])

    id_count = {}

    for id in id_list:

        id_count.setdefault(id, 0)
        id_count[id] += 1

    x = list(set(id_list))
    x.sort()
    
    yLabels = [count for i, count in id_count.items()]

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, yLabels, color = "#1e90ff")
    plt.xlabel("Student ID No.")
    plt.ylabel("Number Of Students (Count)")
    plt.title("ID Wise Stduent Count")

    plt.xticks(x_pos, x)

    plt.show()

show_barChart()