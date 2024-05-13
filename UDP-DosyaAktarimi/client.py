import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 80)

filename = "ornek.txt"
client_socket.sendto(filename.encode(), server_address)

with open(filename, 'rb') as file:
    while True:
        data = file.read(65507)
        if not data:
            break
        client_socket.sendto(data, server_address)

print("Dosya gönderildi.")
