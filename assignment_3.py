import math
import matplotlib.pyplot as plt

total_class = 16

attendance_count = { "70": 0, "60": 0, "45": 0, "30": 0 }

datas = [
    { "name": "Waasay Anwar", "id": "1130715", "attendance": 
        [False, False, False, True, True, False, False, True, True, True, True, False, True, False, True, True], 
        "percentage": 0, "marks": 0 },

    { "name": "Sumon Ahmad", "id": "1310173", "attendance": 
        [False, False, True, False, True, False, True, True, True, True, True, True, True, True, True, True], 
        "percentage": 0, "marks": 0 },
    
    { "name": "Abdullah All Rakib", "id": "1420443", "attendance": 
        [True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True], 
        "percentage": 0, "marks": 0 },

    { "name": "Md. Zillur Rahman", "id": "1510157", "attendance": 
        [True, True, True, True, True, True, True, True, False, True, True, False, True, True, False, True], 
        "percentage": 0, "marks": 0 },

    { "name": "Kazi Sabbir Anwar", "id": "1511242", "attendance": 
        [True, True, False, True, True, True, True, True, True, True, True, True, True, True, False, True], 
        "percentage": 0, "marks": 0 },
    
    { "name": "Sumaiya Habib Poushy", "id": "1511466", "attendance": 
        [True, True, False, True, True, True, True, True, True, True, True, True, True, True, False, True], 
        "percentage": 0, "marks": 0 },

    { "name": "Ezab Quader", "id": "1512081", "attendance": 
        [True, False, False, True, False, False, True, False, True, False, True, True, True, False, False, True], 
        "percentage": 0, "marks": 0 },

    { "name": "S.M Nasif Sadiq", "id": "1530117", "attendance": 
        [False, False, False, True, True, False, True, True, False, True, True, False, True, True, False, False], 
        "percentage": 0, "marks": 0 },

    { "name": "Sadia Afroz", "id": "1530140", "attendance": 
        [False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True], 
        "percentage": 0, "marks": 0 },

    { "name": "Razib Sikder", "id": "1530852", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, False, True, True, True, False, False], 
        "percentage": 0, "marks": 0 },

    { "name": "Abdullah Al Mamun", "id": "1530117", "attendance": 
        [False, False, False, True, True, True, False, True, True, True, True, True, True, False, True, True], 
        "percentage": 0, "marks": 0 },

    { "name": "Md. Rakib Imtiaz", "id": "1610294", "attendance": 
        [False, False, True, True, False, False, True, False, False, True, False, True, True, False, True, True], 
        "percentage": 0, "marks": 0 },

    { "name": "Inkiad Md. Abrar", "id": "1610596", "attendance": 
        [True, True, False, True, True, True, False, True, True, True, False, False, True, False, False, False], 
        "percentage": 0, "marks": 0 },
    
    { "name": "Md. Adib Shahriar", "id": "1610834", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        "percentage": 0, "marks": 0 },

    { "name": "Durjoy Dass", "id": "1610834", "attendance": 
        [False, False, False, False, True, False, True, True, True, True, True, False, True, True, True, True],
        "percentage": 0, "marks": 0 },

    { "name": "Ucchawas", "id": "1620016", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        "percentage": 0, "marks": 0 },

    { "name": "S.M. Iftikhar Rasha", "id": "1620221", "attendance": 
        [True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True],
        "percentage": 0, "marks": 0 },
    
    { "name": "Marufa Tasnim", "id": "1620287", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        "percentage": 0, "marks": 0 },
    
    { "name": "Moshedul Bari Antor", "id": "1620345", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True],
        "percentage": 0, "marks": 0 },

    { "name": "Md. Raian Hossain", "id": "1620363", "attendance": 
        [False, False, False, True, True, False, True, True, False, False, True, True, True, True, False, False],
        "percentage": 0, "marks": 0 },

    { "name": "Assadujjaman Nayeem", "id": "1620538", "attendance": 
        [True, True, False, True, True, True, True, False, True, True, True, True, True, False, False, True],
        "percentage": 0, "marks": 0 },

    { "name": "Md. Golam Shakir", "id": "1620198", "attendance": 
        [True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True],
        "percentage": 0, "marks": 0 },

    { "name": "Md. Yeasir Hossain", "id": "1620601", "attendance": 
        [True, True, False, True, True, True, True, True, True, False, False, True, True, True, False, True],
        "percentage": 0, "marks": 0 },

    { "name": "Ankur Saha", "id": "1620753", "attendance": 
        [False, False, True, True, True, True, False, False, True, False, True, True, True, True, True, True],
        "percentage": 0, "marks": 0 },

    { "name": "Shazid Hasan Riam", "id": "1621060", "attendance": 
        [True, True, False, True, True, True, True, False, True, True, True, False, True, True, False, False],
        "percentage": 0, "marks": 0 },

    { "name": "Tahrim Faroque Tushar", "id": "1621148", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        "percentage": 0, "marks": 0 },

    { "name": "Maliha Mamtaz", "id": "1621418", "attendance": 
        [False, False, True, False, True, False, True, True, False, True, False, True, True, True, False, False],
        "percentage": 0, "marks": 0 },

    { "name": "Nadim Mahmud Dipu", "id": "1711097", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        "percentage": 0, "marks": 0 },
    
    { "name": "Sifatul Alam Shohan", "id": "1711385", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        "percentage": 0, "marks": 0 },

    { "name": "Refat Chowdhury", "id": "1711443", "attendance": 
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        "percentage": 0, "marks": 0 },

    { "name": "Mushfiqur Rahman", "id": "1711552", "attendance": 
        [True, True, True, True, True, True, True, False, True, False, True, False, True, False, True, False],
        "percentage": 0, "marks": 0 }  
]

def individual_report():

    for data in datas:
        count = sum(data["attendance"])
        data["percentage"] = math.ceil(count * 100 / total_class)

    for data in datas:
        if data["percentage"] >= 70:
            data["marks"] = 5
        elif data["percentage"] >= 60:
            data["marks"] = 4
        elif data["percentage"] >= 45:
            data["marks"] = 3
        elif data["percentage"] >= 30:
            data["marks"] = 2

    print("------------------------------------------------------")
    print("Calculated Attendance Percentage")
    print("------------------------------------------------------")
    print("No.\t\tName\t\t\tID\t\t\tPercentage\t\tMarks")

    count = 1

    for data in datas:
        print("{}{}{}\t\t\t\t{}\t\t{}".format(count, data["name"].rjust(24), data["id"].rjust(20), data["percentage"], data["marks"]))
        count = count + 1

def attendance_percentage():

    global attendance_count
    
    for data in datas:
        if data["percentage"] >= 70:
            attendance_count["70"] += 1
        elif data["percentage"] >= 60:
            attendance_count["60"] += 1
        elif data["percentage"] >= 45:
            attendance_count["45"] += 1
        elif data["percentage"] >= 30:
            attendance_count["30"] += 1

    print("------------------------------------------------------")
    print("Attendance Percentage (Student Count)")
    print("------------------------------------------------------")
    print("No.\tPercentage\tCount")

    count = 1

    for data in attendance_count.keys():
        print("{}\t{}\t\t{}\t".format(count, data, attendance_count[data]))
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





def extract_id():
    
    id_list = []
    
    for data in datas:
        id_list.append(data["id"][0:3])

    return id_list

def count_id():

    id_list = extract_id()
    id_count = {}

    for id in id_list:

        id_count.setdefault(id, 0)
        id_count[id] += 1

    return id_count

individual_report()
attendance_percentage()

def print_barchart():

    x = list(set(extract_id()))
    x.sort()
    id_count = count_id()
    
    yLabels = [count for i, count in id_count.items()]

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, yLabels, color = "blue")
    plt.xlabel("Student ID")
    plt.ylabel("Number Of Students")
    plt.title("ID Wise Stduent Count")

    plt.xticks(x_pos, x)

    plt.show()

print_barchart()