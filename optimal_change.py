def optimal_change(item_cost, amount_paid):
    change_due = amount_paid - item_cost
    num_value = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]#highest to lowest to subtract largest possible value 
    coin_word_value = {0.25:'quarter', 0.10: 'dime', 0.05: 'nickel', 0.01: 'penny'}
    money_log = {} #to keep track of each monetary denomination needed and its quantity
    result = "The optimal change for an item that costs "

    #result should only show the money value as a float if there are cents involved. If not, show whole number
    if isinstance(item_cost, float):
        result += f"${item_cost:.2f}"
    else:
        result += f"${item_cost}" 
    result += " with an amount paid of " 
    if isinstance(amount_paid, float):
        result += f"${amount_paid:.2f} is"
    else:
        result += f"${amount_paid} is"

    #if the customer pays and still owes money vs. pays exact amount vs. pays more and requires change
    if amount_paid < item_cost:
        return f"You still owe ${item_cost - amount_paid}."
    elif amount_paid == item_cost:
        return "You paid in exact change. Have a nice day!"
    while change_due > 0: #subtract the highest possible monetary value from the change due, using our monetary value list. Once a value is subtracted, restart the loop.
        for value in num_value:
            if value <= change_due: #every time a value is subtracted, update in our dictionary to keep track of quantity of each value 
                change_due = round(change_due - value,2)
                if value in money_log:
                    money_log[value] += 1
                else:
                    money_log[value] = 1
                break

    counter = len(money_log) #to keep track of when to add ", and" to the result (will need this later)
    more_than_one_type = len(money_log) #if only 1 denomination type needed, forgo using ", and" (will need this later)
    for m in money_log: #for each denomination in our log,
        if m > 0.25 and money_log[m] == 1: #if it's a bill and only 1 quantity
            result += f" 1 ${m} bill"
        elif m > 0.25 and money_log[m] > 1: #if it's a bill and >1 quantity 
            result += f" {money_log[m]} ${m} bills"
        else:
            for c in coin_word_value: #to check if the denomination is a coin
                if m == c and money_log[m] == 1: #if it's a coin and just 1 quantity
                    result += f" 1 {coin_word_value[c]}"
                elif m == c and money_log[m] > 1: #if it's a coin and more than one quantity...
                    if m > 0.01:
                        result += f" {money_log[m]} {coin_word_value[c]}s" #if it's not a penny, simply make plural
                    else:
                        result += f" {money_log[m]} pennies" #if it's a penny, use 'pennies' instead of 'penny'
        counter -= 1 #after each denomination type is accounted for, decrease our counter by 1
        if counter > 1: #if this round was not the last denomination type, add a comma
            result += ','
        if more_than_one_type > 1: #if we had more than one denomination type and this is the last one, add ", and"
            if counter == 1:
                result += ', and'
    result += '.' #finish the sentence with a period
    return result
