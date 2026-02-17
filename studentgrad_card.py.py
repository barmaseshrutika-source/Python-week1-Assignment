marks1 = float(input("Enter marks 1: "))
marks2 = float(input("Enter marks 2: "))
marks3 = float(input("Enter marks 3: "))

average = (marks1 + marks2 + marks3) / 3
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

