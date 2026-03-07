import csv

employees = [
["Sarah Colin",14569,0,40,20],
["Anna Johnson",14572,0,40,22],
["Jessica Dean",14580,3,40,18],
["Taylor Cane",14528,1,40,16],
["Jackson Davis",14530,0,60,16],
["Austin Joan",14532,2,40,16],
["Nathan Lee",14582,0,40,16],
["Bailey Walt",14563,0,50,22],
["Brittney Greene",14520,4,40,18],
["Leann Clancy",14519,0,50,22]
]
file = open("payroll_results.csv","w",newline="")
writer = csv.writer(file)

writer.writerow(["Name","ID","Dependents","Hours","Rate","Gross Pay","State Tax","Federal Tax","Pre-Tax","Post-Tax"])

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