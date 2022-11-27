from optimal_change import optimal_change

print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print("3:", optimal_change(20.08, 50.25) == "The optimal change for an item that costs $20.08 with an amount paid of $50.25 is 1 $20 bill, 1 $10 bill, 1 dime, 1 nickel, and 2 pennies.")
print("4:", optimal_change(1, 1.01) == "The optimal change for an item that costs $1 with an amount paid of $1.01 is 1 penny.")
print("5:", optimal_change(1.50, 100) == "The optimal change for an item that costs $1.50 with an amount paid of $100 is 1 $50 bill, 2 $20 bills, 1 $5 bill, 3 $1 bills, and 2 quarters.")
print("6:", optimal_change(0.25, 1) == "The optimal change for an item that costs $0.25 with an amount paid of $1 is 3 quarters.")
print("7:", optimal_change(0.01, 10) == "The optimal change for an item that costs $0.01 with an amount paid of $10 is 1 $5 bill, 4 $1 bills, 3 quarters, 2 dimes, and 4 pennies.")
print("8:", optimal_change(5.22, 5.25) == "The optimal change for an item that costs $5.22 with an amount paid of $5.25 is 3 pennies.")
print("9:", optimal_change(1.50, 5.50) == "The optimal change for an item that costs $1.50 with an amount paid of $5.50 is 4 $1 bills.")
print("10:", optimal_change(10, 10) == "You paid in exact change. Have a nice day!")
print("11:", optimal_change(300, 100) == "You still owe $200.")
print("12:", optimal_change(15,14) == "You still owe $1.")
