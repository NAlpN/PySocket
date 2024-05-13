import socket
import cv2
import numpy as np

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 80)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    encoded_frame = cv2.imencode('.jpg', frame)[1]
    data = encoded_frame.tobytes()

    client_socket.sendto(data, server_address)

cap.release()
client_socket.close()