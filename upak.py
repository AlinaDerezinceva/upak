students = []

with open("students.txt", "r") as file:
    for line in file:
        s = line.strip().split(";") 
        student = {
            'id': int(s[0]),
            'full_name': s[1],
            'var': int(s[2]),
            'subgroup': int(s[3])
        }
        students.append(student)

print(students)



 

