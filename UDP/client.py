import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)

message = input("Mesajınız: ")
client_socket.sendto(message.encode(), server_address)

response, server_address = client_socket.recvfrom(1024)
print("Sunucudan gelen yanıt:", response.decode())