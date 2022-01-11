
class Account:

    def __init__(self, number, holder, balance, limit):
        print(f"Building a object...{self}.")
        self.__number    = number
        self.__holder    = holder
        self.__balance   = balance
        self.__limit     = limit
        self.__bank_code = "001"

    def statement(self):
        print(f"The holder {self.__holder} has R$ {self.__balance}.")

    def deposit(self, value):
        self.__balance += value

    def __available_withdraw(self, value):
        value_available_to_withdraw = self.__balance + self.__limit
        return value <= value_available_to_withdraw

    def withdraw(self, value):
        if self.__available_withdraw(value):
            self.__balance -= value
        else:
            print(f"The value {value} does not fit within your limit.")

    def transfer(self, valor, account_destiny):
        self.withdraw(valor)
        account_destiny.deposita(valor)

    def get_balance(self):
        return self.__balance

    def get_holder(self):
        return self.__holder

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def banks_codes():
        return {"BB":"001","Caixa":"104", "Bradesco":"237"}
