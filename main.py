print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? S$"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
peoples = int(input("How many people to split the bill?"))
total_tip = tip/100 * bill
bill_with_tip = total_tip + bill
final_amount = bill_with_tip/peoples
print(f"Final amount need to pay per pax is S$ {final_amount}")

