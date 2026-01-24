# Assignment 1: Total and Average of Three Subjects

def calculate_total_average(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))

total, average = calculate_total_average(sub1, sub2, sub3)

print("Total Marks:", total)
print("Average Marks:", average)
