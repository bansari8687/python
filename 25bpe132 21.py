def calculate_net_salary(gross_salary):
    allowance = gross_salary * 0.10
    deduction = gross_salary * 0.03
    net_salary = gross_salary + allowance - deduction
    return allowance, deduction, net_salary

gross = float(input("Enter Gross Salary: "))

allowance, deduction, net = calculate_net_salary(gross)

print("Allowance (10%):", allowance)
print("Deduction (3%):", deduction)
print("Net Salary:", net)
