#Justin Kilgo
#010828946

import socket

HOST = 'localhost'
PORT = 65432

class BankAccount:
    def __init__(self):
        self.balance = 100
    
    def check_balance(self):
        return str(self.balance)
    
    def deposit(self, amount):
        try:
            amount = int(amount)
            if amount < 0 or amount % 1 != 0:
                raise ValueError
        except ValueError:
            return 'Please enter a valid amount to deposit (a positive integer)'
        
        self.balance += amount
        return (self.balance, amount)
    
    def withdraw(self, amount):
        try:
            amount = int(amount)
            if amount < 0 or amount % 1 != 0:
                raise ValueError
            elif amount > self.balance:
                return f'You do not have enough money to withdraw ${amount}.'
        except ValueError:
            return 'Please enter a valid amount to withdraw (a positive integer)'
        
        self.balance -= amount
        return (self.balance, amount)

def main():
    bank_account = BankAccount()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            data = None
            with conn:
                print(f"Connected by {addr}")
                while conn:
                    data = conn.recv(1024)
                    if data.decode() == '':
                        break
                    data = data.decode().split(',')
                    message = ''
                    if data[0] == 'check balance':
                        print('check')
                        message = f'Your current balance is ${bank_account.check_balance()}'
                    elif data[0] == 'deposit':
                        print('deposit')
                        message = bank_account.deposit(data[1])
                        if type(message) is tuple:
                            message = f'You have deposited ${message[1]}. Your new balance is ${message[0]}.'
                    elif data[0] == 'withdraw':
                        print('withdraw')
                        message = bank_account.withdraw(data[1])
                        if type(message) is tuple:
                            message = f'You have withdrawn ${message[1]}. Your new balance is ${message[0]}'
                    elif data[0] == 'close':
                        print('Goodbye!')
                        exit()
                    
                    conn.sendall(message.encode())
                print(f'Disconnected from {addr}')
        
if __name__ == '__main__':
    main()