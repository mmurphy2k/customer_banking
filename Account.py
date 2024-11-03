""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the account"""
        self.interest = interest

    # This method gets the balance of the account.
    def get_balance(self):
        """Gets the balance for the account"""
        return self.balance

    # The method gets the interest gained for the account.
    def get_interest(self):
        """Gets the interest gained for the account"""
        return self.interest