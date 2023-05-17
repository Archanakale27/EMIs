def calculate_emi(principal, tenure, interest_rate):
    # Convert interest rate from percentage to decimal
    interest_rate = interest_rate / (100 *12)

    # Convert tenure from years to months
    tenure = tenure * 12

    # Calculate EMI
    emi = (principal * interest_rate * (1 + interest_rate) ** tenure) / ((1 + interest_rate) ** tenure - 1)

    return round(emi, 2)


def print_emi():
    # Get user input
    principal = float(input("Enter principal amount: "))
    tenure = int(input("Enter tenure (in years): "))
    interest_rate = float(input("Enter interest rate (% per annum): "))

    # Calculate EMI
    emi = calculate_emi(principal, tenure, interest_rate)

    # Print the result
    print("EMI: ", emi)

# Run the program
print_emi()