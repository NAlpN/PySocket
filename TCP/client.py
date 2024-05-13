import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 80)

client_socket.connect(server_address)

message = input("Mesajınız: ")
client_socket.sendall(message.encode())

response = client_socket.recv(1024)
print("Sunucudan gelen yanıt:", response.decode())

client_socket.close()
