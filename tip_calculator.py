print("Welcome to the tip calculator.")
bill = float(input("What was the bill? $ "))
percentage = int(
    input("What percentage tip would you like to give? 10, 12 , or 15  "))
people = (int(input("How many people to split the bill? ")))
final_bill = (bill*(100+percentage)/100)/people
print(round(final_bill, 2))
