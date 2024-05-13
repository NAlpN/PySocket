import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 80)

server_socket.bind(server_address)

server_socket.listen(5)

print("Sunucu başlatıldı. İstemci bekleniyor...")

client_socket, client_address = server_socket.accept()

print("Bağlantı kabul edildi:", client_address)

data = client_socket.recv(1024)
print("İstemciden gelen veri:", data.decode())

client_socket.sendall("Mesaj alındı. Teşekkürler!".encode())

client_socket.close()
server_socket.close()
