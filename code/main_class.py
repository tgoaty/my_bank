class Bank:

    def __init__(self, name):
        """
        Инициализация банка.
        """
        self.name = name
        self.accounts = {}
        self.count_of_code = 1

    def create_account(self):
        """
        Создает новый банковский счет с уникальным номером.
        """
        self.accounts[self.count_of_code] = 0
        print(f'Account {self.count_of_code} was created.')
        self.count_of_code += 1

    def set_balance(self, account_number, amount):
        """
        Устанавливает баланс указанного счета.
        """
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
        self.accounts[account_number] += amount

    def lose_money(self, account_number, amount):
        """
        Снимает указанную сумму со счета.
        """
        if self.accounts[account_number] < amount:
            print(f'Account {account_number} does not have enough money.')
        else:
            self.accounts[account_number] -= amount


my_bank = Bank('Tinkon')
while True:
    message = input('Command: ')
    if message == 'q':
        break
    elif message == 'ca':
        my_bank.create_account()
    elif message == 'sb':
        account_number = int(input('Account number: '))
        amount = int(input('Amount: '))
        my_bank.set_balance(account_number, amount)
    elif message == 'tm':
        from_account = int(input('From account number: '))
        to_account = int(input('To account number: '))
        amount = int(input('Amount: '))
        my_bank.transfer_money(from_account, to_account, amount)
    elif message == 'la':
        my_bank.list_accounts()
    elif message == 'gm':
        account_number = int(input('Account number: '))
        amount = int(input('Amount: '))
        my_bank.get_money(account_number, amount)
    elif message == 'lm':
        account_number = int(input('Account number: '))
        amount = int(input('Amount: '))
        my_bank.lose_money(account_number, amount)
    else:
        print('Invalid command.')
