import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 80)

server_socket.bind(server_address)

print("UDP Sunucu başlatıldı. İstemci bekleniyor...")

filename, addr = server_socket.recvfrom(1024)
filename = filename.decode()
print("Alınan dosya adı:", filename)

file = open(filename, 'wb')

while True:
    data, addr = server_socket.recvfrom(65507)
    if not data:
        break
    file.write(data)

file.close()
print("Dosya alındı.")
