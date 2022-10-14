#Justin Kilgo
#010828946

import socket
from server import PORT, HOST

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        print('''\nHello! Welcome to my HW6 Banking Software. 
You begin with $100, you may check balance, deposit, or withdraw. 
To do any of these, simply type 'deposit', 'withdraw', or 'check balance'. If you would like to exit, type 'exit'.
For simplicity, keep everything lowercase and type exactly as stated above (amounts will be prompted afterwards).
If you would like to exit both the client and the server, type 'close'.\n''')
        while (s):
            action = input('Would you like to deposit, withdraw, check balance, or exit?\n').strip()
            if action == 'exit' or action == 'close':
                print('Goodbye!\n')
                if action == 'close':
                    message = f'{action},'
                    s.sendall(message.encode())
                break
            elif action == 'check balance':
                message = f'{action},'
            elif action == 'deposit':
                deposit = input('How much would you like to deposit?\n')
                message = f'{action},{deposit}'
            elif action == 'withdraw':
                withdraw = input('How much would you like to withdraw?\n')
                message = f'{action},{withdraw}'
            else:
                print('Please enter a valid request (check balance, deposit, withdraw).')
                continue
            
            s.sendall(message.encode())
            data = s.recv(1024)
            if data.decode() == '':
                print('Server was disconnected\n')
                break
            else:
                print(data.decode())
            
            print()

if __name__ == '__main__':
    main()