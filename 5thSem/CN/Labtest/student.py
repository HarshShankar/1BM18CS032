import socket;

HOST='49.207.210.112'
PORT= 65402

print('-------------------------STUDENT----------------------')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
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
