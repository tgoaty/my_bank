from main_class import Bank


def process():
    my_bank = Bank('Tinkon')
    while True:
        message = input('Command: ').lower()
        if message == 'q':
            break

        elif message == 'ca':
            my_bank.create_account()

        elif message.startswith('ca*'):
            for i in range(int(message[3:])):
                my_bank.create_account()

        elif message == 'sb':
            account_number = input('Account number: ')
            amount = input('Amount: ')
            my_bank.set_balance(account_number, amount)

        elif message == 'tm':
            from_account = input('From account number: ')
            to_account = input('To account number: ')
            amount = input('Amount: ')
            my_bank.transfer_money(from_account, to_account, amount)

        elif message == 'la':
            my_bank.list_accounts()

        elif message == 'gm':
            account_number = input('Account number: ')
            amount = input('Amount: ')
            my_bank.get_money(account_number, amount)

        elif message == 'lm':
            account_number = input('Account number: ')
            amount = input('Amount: ')
            my_bank.lose_money(account_number, amount)

        elif message == 'cb':
            my_bank.capital_balance()

        else:
            print('Invalid command.')


if __name__ == '__main__':
    process()
