# servidor.py
import socket
import uuid
import time
from datetime import datetime

LOG_FILE = "server_log.txt"
SERVER_HOST = "0.0.0.0" 
SERVER_PORT = 0000

def log_connection(client_ip, client_name, client_id, timestamp):
    with open(LOG_FILE, "a") as f:
        log_entry = f"{datetime.now()} - IP: {client_ip}, Name: {client_name}, UUID: {client_id}, Timestamp: {timestamp}\n"
        f.write(log_entry)

def start_server():
    print(f"Servidor escuchando en {SERVER_HOST}:{SERVER_PORT}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()

    while True:
        client_socket, client_address = server_socket.accept()
        client_ip = client_address[0]
        print(f"\nConexión recibida de {client_ip}")

        client_name = client_socket.recv(1024).decode()
        client_id = str(uuid.uuid4())
        timestamp = str(time.time())

        client_socket.send(f"{timestamp},{client_id}".encode())
        client_socket.close()

        log_connection(client_ip, client_name, client_id, timestamp)
        print(f"Registrado: {client_name} ({client_ip}) UUID: {client_id} Timestamp: {timestamp}")

if __name__ == "__main__":
    start_server()
