import socket
import cv2
import numpy as np

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 80)

server_socket.bind(server_address)

print("UDP Sunucu başlatıldı. İstemci bekleniyor...")

while True:
    data, client_address = server_socket.recvfrom(65507)
    frame = np.frombuffer(data, dtype=np.uint8)

    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow("Görüntü", frame)
    cv2.waitKey(1)