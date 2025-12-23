# ShadowShell 🛡️

**ShadowShell** is a custom lightweight Reverse Shell framework built in Python. It demonstrates the mechanics of Command & Control (C2) infrastructure, client-server socket communication, and remote command execution.

## ⚠️ Disclaimer
**FOR EDUCATIONAL PURPOSES ONLY.**
This tool was developed to understand the underlying mechanics of reverse shells and network defense. It is intended for use only on systems you own or have explicit permission to test. The author is not responsible for any misuse of this tool.

## 🌟 Features
* **Persistent Connection:** Auto-reconnects if the connection drops.
* **Remote Command Execution:** Executes shell commands on the client and retrieves output.
* **Custom Protocol:** Uses raw TCP sockets for communication.

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sreevishnu-sviii/ShadowShell.git](https://github.com/sreevishnu-sviii/ShadowShell.git)
    cd ShadowShell
    ```

2.  **Run the Server (Attacker):**
    ```bash
    python3 c2_server.py
    ```

3.  **Run the Client (Target):**
    ```bash
    python3 c2_client.py
    ```

## 👤 Author
Sreevishnu V - Aspiring Web Application Penetration Tester
