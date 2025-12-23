import socket
HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(1)
print(f"[+] Server is listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"[+] Connected by {addr}")

data = conn.recv(1024).decode()
print(f"[Client]: {data}")

response = "Hello from Server"
conn.send(response.encode())

conn.close()
server.close()
