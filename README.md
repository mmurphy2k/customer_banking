# Customer Banking
## Module 3 Homework Assignment
### Table of Contents
1. **Program Descriptions**
2. **File Structure**
3. **How to run the program**
4. **Account.py**
5. **cd_account.py**
6. **customer_banking.py**
7. **README.md**
8. **savings_account.py**


## 1. **Program Descriptions**

This program is a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.


## 2. **File Structure**

![Screenshot of the GitHub repository for this application.](https://github.com/user-attachments/assets/cb7c562e-9204-4acb-99bd-10cb85865161)


## 3. **How to run the program**

The two ways you can run this program are

1. Within VS Code, select the **"customer_banking.py"** file and select the **[Run Python File]** button in the top right side.
2. From a terminal window, run the following command **"python customer_banking.py"**


## 4. **Account.py**

This file contains the **"Account"** class definition. This class reguires two parameters to initialize, the balance for the account and the interest earned for the account.

      my_account = Account(balance, 0)

Within this class there are four methods defined:

1. **"set_balance()"** method sets the balance for this account.
2. **"set_interest()"** method sets the interest earned for this account.
3. **"get_balance()"** method returns the balance for this account
4. **"get_interest()"** method returns the interest earned for this account. 


## 5. **cd_account.py**

This file contins the **"create_cd_account()"** function definition for the CD Account. This function requires three parameters, the balance for the account, the interest rate for the account, and the number of months until maturity.

    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """


## 6. **customer_banking.py**

This file contains the **"main()"** function, the **"clear_screen()"** function, the **"validate_number()"** function, and the **"user_input"** function.

1. **main()**

       """This function prompts the user to enter the savings and cd account balance, interest rate,
       and the length of months to determine the interest gained.
       It displays the interest earned on the savings and CD accounts and updates the balances.
       This function will call the other functions within this file to help with prompting users for the inputs,
       and validating the information before passing it onto the external functions.
       """

2. **clear_screen()**

       """This function will clear the screen beofre prompting the users for inputs.
       """

3. **validate_number()**

       """This function will validate the user input to be a valid number or not. It will retuen True or False. 
       """

4. **user_input()**

       """This function will prompt the user for the balance, APR interest rate, and the number of months until maturity.
       The function will return the balance, interest, and months to be used elsewhere in the program.
       """


## 7. **README.md**

This file. 


## 8. **savings_account.py**

This file contins the **"create_savings_account()"** function definition for the Savings Account. This function requires three parameters, the balance for the account, the interest rate for the account, and the number of months until maturity.

    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """

---------------------------------------------

Mark Murphy mmurphy2k@gmail.com
