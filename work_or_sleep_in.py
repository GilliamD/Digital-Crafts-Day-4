day = int(input("Day 0-6 "))

if day == 0 or day == 6:
    print("Sleep in")
elif (day > 0) and (day <= 5):
    print("Go to work")
else:
    print("That\'s not a day.")