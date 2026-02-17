num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Prime Check
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")
