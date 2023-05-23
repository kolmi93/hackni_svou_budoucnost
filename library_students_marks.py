students_results = {
    "Harry": 85,
    "Ron": 71,
    "Hermione": 98,
    "Draco":69
}

results = {}
for 
for key in students_results:
    if students_results[key] >= 91:
        students_results[key] == "Excelent"
    elif students_results[key] >= 81 and students_results[key] <= 90:
        students_results[key] == "Vynikající"
    elif students_results[key] >= 71 and students_results[key] <= 80:
        students_results[key] == "Splněno"
    else:
        students_results[key] == "Nesplněno"

print(students_results)