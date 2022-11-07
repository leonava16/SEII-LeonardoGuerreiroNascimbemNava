#importar os modulos
import socket 
import threading

HEADER = 64
PORT = 5050 #Porta de acesso
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) # Endereco
FORMAT = 'utf-8' #Formato de decodificacao
DISCONNECT_MESSAGE = "!DISCONNECT"

#declarar servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# enviar mensagem para unica pessoa:

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()