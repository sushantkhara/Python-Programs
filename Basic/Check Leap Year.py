year = int(input("Enter year to be checked:"))
if year % 4==0 and year %100 != 0 or year %400 == 0:
        print("It is a leap year!", year)
else:
    print(" Not a leap year!", year)
