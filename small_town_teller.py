class Person:
    def __init__(self, id, fname, lname):
        self.id = id
        self.first_name = fname
        self.last_name = lname



class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance



# Here is your Big Hint

class Bank:

    def __init__(self):
        self.customers: Dict[int, Person] = dict()
        self.accounts: Dict[int, Account] = dict()

    def add_customer(self, customer: Person) -> None:
        if customer.id in self.customers:
            raise ValueError(f"Customer with id {customer.id} already exists.")
        else:
            self.customers[customer.id] = customer

    def add_account(self, account: Account):
        if account.owner.id not in self.customers:
            raise ValueError(f"{account.owner.id} is not a valid customer id.")
        elif account.number in self.accounts:
            raise ValueError(f"Account with id {account.number} already exists")
        else:
            self.accounts[account.number] = account

## And another method
    def deposit(self, account_id: int, amount: float):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance += round(amount, 2)
        else:
            raise ValueError(f"Account with id {account_id} does not exist.")