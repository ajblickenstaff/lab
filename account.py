class Account:
    def __init__(self, name: str):
        """
        Initialize the Account object with a given name and a balance of 0.

        :param name: The name of the account holder.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposit a specified amount into the account.

        :param amount: The amount to be deposited.
        :return: True if the deposit transaction is successful, False otherwise.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw a specified amount from the account.

        :param amount: The amount to be withdrawn.
        :return: True if the withdrawal transaction is successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Get the account balance.

        :return: The account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Get the account name.

        :return: The account name.
        """
        return self.__account_name
