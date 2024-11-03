"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the CD Account
def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_account = Account(balance, 0)

    # Test print statements for debugging
    # print(type(cd_account))
    # print(f"Opening CD Balance is: ${cd_account.get_balance():,.2f}")
    # print(f"Opening Interest Earned is: ${cd_account.get_interest():,.2f}")
    # print(f"The APR rate is: {interest_rate:,.2f}%")
    # print("The number of months till mature:", months)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = balance * ((interest_rate / 100) * (months / 12))

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    new_cd_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_balance(new_cd_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_interest(interest_earned)

    # Test print statements for debugging
    # print(f"Updated CD Balance is: ${cd_account.get_balance():,.2f}")
    # print(f"Updated Interest Earned is: ${cd_account.get_interest():,.2f}")

    # Return the updated balance and interest earned.
    return cd_account.get_balance(), cd_account.get_interest() # ADD YOUR CODE HERE
