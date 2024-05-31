
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? like 10, 15 ,20 etc. $ "))
num_people = int(input("How much people to split the bill? "))

split_bill = round((float(total_bill) + float(tip))/int(num_people),2)
print(f"Each person should pay {split_bill}")
