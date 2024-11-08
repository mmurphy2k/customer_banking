# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
import os
import sys

# Define clear_screen function
def clear_screen():
    """ Clear the terminal screen. """
    os.system('cls' if os.name == 'nt' else 'clear')

# Define validate_number function
def validate_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Define user_imput function
def user_input():
    loop = True
    while loop:
        user_balance = input('What is your account balance? ')

        if validate_number(user_balance):
            user_balance = float(user_balance)
            loop = False
        else:
            # sys.exit("This is not a valid deposit amount. Please try again.")
            print("This is not a valid deposit amount. Please try again.")
  
    loop = True
    while loop:
        user_interest = input('What is the APR for the account? ')

        if validate_number(user_interest):
            user_interest = float(user_interest)
            loop = False
        else:
            # sys.exit("This is not a valid APR. Please try again.")
            print("This is not a valid APR. Please try again.")

    loop = True
    while loop:
        user_months = input('How many months until maturity? ')

        if validate_number(user_months):
            user_months = int(user_months)
            loop = False
        else:
            # sys.exit("This is not a valid number. Please try again.")
            print("This is not a valid number. Please try again.")

    return user_balance, user_interest, user_months


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("Please enter the following information for your Savings Account:")
    savings_balance, savings_interest, savings_maturity = user_input()
    # savings_balance = float(input('What is your savings account balance? '))
    # savings_interest = float(input('What is the APR for the savings account? '))
    # savings_maturity = int(input('How many months till maturity? '))

    # Call the create_savings_account function and pass the variables from the user.
    #savings_account = create_savings_account(savings_balance, savings_interest, savings_maturity)
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Test print statements for debugging
    #print(type(savings_account))
    # print(f"Savings Balance is: ${savings_account.balance:,.2f}")
    # print(f"Savings Interest Earned is: ${savings_account.interest:,.2f}")

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Savings Interest Earned is: ${savings_interest_earned:,.2f}")
    print(f"Savings Account Balance is: ${updated_savings_balance:,.2f}")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("\nPlease enter the following information for your CD Account:")
    cd_balance, cd_interest, cd_maturity = user_input()
    # cd_balance = float(input('What is your CD account balance? '))
    # cd_interest = float(input('What is the APR for the CD account? '))
    # cd_maturity = int(input('How many months till maturity? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD Interest Earned is: ${cd_interest_earned:,.2f}")
    print(f"CD Account Balance is: ${updated_cd_balance:,.2f}")


if __name__ == "__main__":
    # Call the main function.
    clear_screen()
    main()
