import socket;

HOST='127.0.0.1'
PORT= 54321

print('-------------------------CLIENT----------------------')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        while True:
            filename= input('Enter the file name: ');

            if not filename:
                break;

            sock.sendall(bytes(filename,'utf8'))
            print(f'Sent: {filename}')

            data= sock.recv(1024).decode('utf-8')
            print(f'Received: {data}')
            print()
