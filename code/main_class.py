class Bank:

    def __init__(self, name):
        """
        Инициализация банка.
        """
        self.name = name
        self.accounts = {}
        self.count_of_code = 1

    def create_account(self):
        import random
        """
        Создает новый банковский счет с уникальным номером.
        """
        self.accounts[str(self.count_of_code)] = 0
        print(f'Account {self.count_of_code} was created.')
        self.count_of_code += random.randint(1, 10)

    def set_balance(self, account_number, amount):
        """
        Устанавливает баланс указанного счета.
        """
        amount = int(amount)
        if account_number.lower() == 'all':
            for v, k in self.accounts.items():
                self.accounts[v] = k + amount
                print(f'Account {v} got balance: {k + amount}.')
        else:
            self.accounts[account_number] = amount
            print(f'Account {account_number} got balance: {amount}.')

    def get_balance(self, account_number):
        """
        Возвращает баланс указанного счета.
        """
        balance = self.accounts[account_number]
        print(f'{account_number} balance: {self.accounts[account_number]}')
        return balance

    def transfer_money(self, from_account, to_account, amount):
        """
        Переводит средства с одного счета на другой.
        """
        amount = int(amount)
        if self.accounts[from_account] < amount:
            print(f'Account {from_account} does not have enough money.')
        else:
            self.accounts[from_account] -= amount
            self.accounts[to_account] += amount

    def list_accounts(self):
        """
        Выводит список всех счетов в банке.
        """
        print(self.name)
        for v, k in self.accounts.items():
            print(f'{v}:  {k}')

    def get_money(self, account_number, amount):
        """
        Пополняет счет указанной суммой.
        """
        amount = int(amount)
        self.accounts[account_number] += amount

    def lose_money(self, account_number, amount):
        """
        Снимает указанную сумму со счета.
        """
        amount = int(amount)
        if self.accounts[account_number] < amount:
            print(f'Account {account_number} does not have enough money.')
        else:
            self.accounts[account_number] -= amount

