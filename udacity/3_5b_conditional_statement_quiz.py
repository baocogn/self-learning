state = str(input())
purchase_amount = float(input())

if state == "Yes":
    tax_amount = 0.075
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you said {}, your total cost is {}.".format(state, total_cost)
elif state == "No":
    tax_amount = 0.095
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you said {}, your total cost is {}.".format(state, total_cost)

print(result)