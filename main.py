print("Welcome to the tip calculator")
bill = float(input("Type in the total bill? $ "))
tip_percentage = int(input("Type in the percentage tip you would like to give? 10, 12, or 15: %"))
party_size = int(input("How many people to split the bill?"))
tip = (tip_percentage / 100) * bill 
total_bill = bill + tip
cost_per_head = (total_bill / party_size)
final_bill = round(cost_per_head, 2)
final_bill = "{:.2f}".format(cost_per_head, 2)
print(f"You each owe: ${final_bill}")