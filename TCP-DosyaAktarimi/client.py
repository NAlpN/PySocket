import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 80)

client_socket.connect(server_address)

filename = "ornek.txt"
client_socket.send(filename.encode())

with open(filename, 'rb') as file:
    while True:
        data = file.read()
        if not data:
            break
        client_socket.sendall(data)

print("Dosya gönderildi.")
