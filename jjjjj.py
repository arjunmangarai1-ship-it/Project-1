
class Account: # class name #parent class
    def __init__(bank, holder, balance): # this is constructor
        bank.holder = holder        
        bank.__balance = balance  # private variable  

    def get_balance(bank):# get method
        return bank.__balance

    def show_details(bank):
        print(f"Holder: {bank.holder}, Balance: {bank.__balance}")


class SavingsAccount(Account):# child class
    def __init__(bank, holder, balance, interest):
        super().__init__(holder, balance)
        bank.interest = interest

    def show_details(bank):
        print(f"Holder: {bank.holder}, Balance: {bank.get_balance()}, Interest: {bank.interest}%")

acc1 = Account("Arjun", 20000)# object
acc2 = SavingsAccount("Ravi", 50000, 5)

acc1.show_details()#calling
acc2.show_details()
