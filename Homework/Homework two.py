try:
    gross = float(input("Gross salary? : "))
    children = int(input("How many children do you have?: "))

    if gross < 1000:
        tax = 0.10
    elif gross < 2000:
        tax = 0.12
    elif gross < 4000:
        tax = 0.14
    else:
        tax = 0.18
    if gross < 2000:
        tax = tax - (children * 0.01)
    else:
        tax = tax - (children * 0.005)

    net = gross - (gross * tax)

    print("Net salary is:", net)

except:
    print("Please give valid numbers")
