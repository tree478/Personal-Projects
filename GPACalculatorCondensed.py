AP = {
  "A+" : 5.7,
  "A" : 5.3,
  "A-" : 5,
  "B+" : 4.7,
  "B" : 4.3,
  "B-" : 4,
  "C+" : 3.7,
  "C" : 3.3,
  "C-": 3,
  "D+" : 2.7,
  "D" : 2.3,
  "D-" : 2,
  "F" : 0
}

Honors = {
  "A+" : 5.2,
  "A" : 4.8,
  "A-" : 4.5,
  "B+" : 4.2,
  "B" : 3.8,
  "B-" : 3.5,
  "C+" : 3.2,
  "C" : 2.8,
  "C-": 2.5,
  "D+": 2.2,
  "D" : 1.7,
  "D-" : 1.5,
  "F" : 0
}

ALevel = {
  "A+" : 4.7,
  "A" : 4.3,
  "A-" : 4,
  "B+" : 4.7,
  "B" : 3.3,
  "B-" : 3,
  "C+" : 2.7,
  "C" : 2.3,
  "C-": 2,
  "D+": 1.7,
  "D" : 1.3,
  "D-" : 1,
  "F" : 0
}

total_number_of_classes = 0
add_another_class = input("Do you want to add a class ? (yes/no)")
sum_of_grades = 0
while add_another_class != "no":
    total_number_of_classes += 1
    weight = (input("What level is your class?(ALevel, Honors, AP)"))
    grade = (input("What grade do you have in that class?(A+, A, A-, B+...)"))
    if weight == "AP":
        sum_of_grades = sum_of_grades + AP[grade]
    elif weight == 'Honors':
        sum_of_grades = sum_of_grades + Honors[grade]
    else:
        sum_of_grades = sum_of_grades + ALevel[grade]

    add_another_class = input("Do you want to add a class ? (yes/no)")

finalGPA = sum_of_grades / total_number_of_classes

print("Your GPA is", finalGPA)