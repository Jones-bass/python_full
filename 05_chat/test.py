import socket

HOST = "127.0.0.1"
PORT = 55556

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

if client.recv(1024) == b"SALA":
    client.sendall(b"Games\n")
    client.sendall(b"Jones\n")

while True:
    texto = input("> ")
    client.send(texto.encode())