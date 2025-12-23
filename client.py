import socket

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("[+] Connected to server")

msg = "Hello Server"
client.send(msg.encode())

reply = client.recv(1024).decode()
print(f"[Server]: {reply}")

client.close()
