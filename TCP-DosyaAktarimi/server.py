import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 80)

server_socket.bind(server_address)

server_socket.listen(1)

print("TCP Sunucu başlatıldı. İstemci bekleniyor...")

client_socket, client_address = server_socket.accept()

filename = client_socket.recv(1024).decode()
print("Alınan dosya adı:", filename)

file = open(filename, 'wb')

while True:
    data = client_socket.recv()  
    if not data:
        break
    file.write(data)

file.close()
print("Dosya alındı.")
