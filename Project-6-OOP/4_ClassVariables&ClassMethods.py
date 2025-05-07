# Bank class uses a class variable and class method to update and reflect bank name across instances.

class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
Bank.change_bank_name("National Bank")
print(b1.bank_name)
print(b2.bank_name)