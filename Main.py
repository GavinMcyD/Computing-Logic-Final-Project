import csv

file = open("payroll_results.csv","w",newline="")
writer = csv.writer(file)

writer.writerow(["Name","ID","Dependents","Hours","Rate","Gross Pay","State Tax","Federal Tax","Pre-Tax","Post-Tax"])

employees = []

while True:
    name = input("Enter employee name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    emp_id = input("ID: ")
    dependents = int(input("Dependents: "))
    hours = float(input("Hours worked: "))
    rate = float(input("Hourly rate: "))

    employees.append([name, emp_id, dependents, hours, rate])

for emp in employees:

    name = emp[0]
    emp_id = emp[1]
    dependents = emp[2]
    hours = emp[3]
    rate = emp[4]

    if hours <= 40:
        gross = hours * rate
    else:
        gross = (40 * rate) + ((hours - 40) * rate * 1.5)

    state_tax = gross * 0.056
    federal_tax = gross * 0.079
    pre_tax = gross
    post_tax = gross - state_tax - federal_tax

    writer.writerow([name,emp_id,dependents,hours,rate,gross,state_tax,federal_tax,pre_tax,post_tax])

file.close()

print("Spreadsheet created: payroll_results.csv")