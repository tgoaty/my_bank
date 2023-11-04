class Bank:

    def __init__(self, name):
        """
        Инициализация банка.
        """
        self.name = name
        self.accounts = {}
        self.count_of_code = 1
        self.capital = 0

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
        if amount.isdigit():
            amount = int(amount)
            if account_number.lower() == 'all':
                for v, k in self.accounts.items():
                    self.accounts[v] = k + amount
                    print(f'Account {v} got balance: {k + amount}.')
            else:
                self.accounts[account_number] = amount
                print(f'Account {account_number} got balance: {amount}.')
        else:
            print('Invalid amount.')
            pass

    def get_balance(self, account_number):
        """
        Возвращает баланс указанного счета.
        """
        balance = self.accounts[account_number]
        print(f'{account_number} balance: {self.accounts[account_number]}')

    def capital_balance(self):
        """
        Возвращает баланс банка.
        """
        self.capital = sum([k for k in self.accounts.values()])
        print(f'Capital balance: {self.capital}')

    def transfer_money(self, from_account, to_account, amount):
        """
        Переводит средства с одного счета на другой.
        """
        if amount.isdigit():
            amount = int(amount)
            if self.accounts[from_account] < amount:
                print(f'Account {from_account} does not have enough money.')
            else:
                self.accounts[from_account] -= amount
                self.accounts[to_account] += amount
        else:
            print('Invalid amount.')
            pass

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
        if amount.isdigit():
            amount = int(amount)
            self.accounts[account_number] += amount
        else:
            print('Invalid amount.')
            pass
        self.capital_balance()

    def lose_money(self, account_number, amount):
        """
        Снимает указанную сумму со счета.
        """
        if amount.isdigit():
            amount = int(amount)
            if self.accounts[account_number] < amount:
                print(f'Account {account_number} does not have enough money.')
            else:
                self.accounts[account_number] -= amount
        else:
            print('Invalid amount.')
            pass
        self.capital_balance()
