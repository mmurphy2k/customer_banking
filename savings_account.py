"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    savings_account = Account(balance, 0)

    # Test print statements for debugging
    #print(type(savings_account))
    # print(f"Opening Savings Balance is: ${savings_account.get_balance():,.2f}")
    # print(f"Opening Interest Earned is: ${savings_account.get_interest():,.2f}")
    # print(f"The APR rate is: {interest_rate:,.2f}%")
    # print("The number of months till mature:", months)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = balance * ((interest_rate / 100) * (months / 12))
 
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    new_savings_balance = balance + interest_earned
    
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(new_savings_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(interest_earned)

    # Test print statements for debugging
    # print(f"Updated Savings Balance is: ${savings_account.get_balance():,.2f}")
    # print(f"Updated Interest Earned is: ${savings_account.get_interest():,.2f}")

    # Return the updated balance and interest earned.
    #return (savings_account) # ADD YOUR CODE HERE
    return savings_account.get_balance(), savings_account.get_interest()
