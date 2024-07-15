import socket
from pymavlink import mavutil
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 14550))

connection = mavutil.mavlink_connection('udp:localhost:14550')

def check_connection():
    heartbeat = connection.recv_match(type='HEARTBEAT', blocking=True)
    if heartbeat:
        print(f"Connected to vehicle, mode: {heartbeat.custom_mode}")

def arm_vehicle():
    connection.arducopter_arm()
    connection.motors_armed_wait()

def disarm_vehicle():
    connection.arducopter_disarm()
    connection.motors_disarmed_wait()

def go_to_position(x, y, z):
    msg = connection.message_factory.set_position_target_local_ned_encode(
        0,
        0, 0,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b0000111111111000,
        x, y, -z,
        0, 0, 0,
        0, 0, 0,
        0, 0)
    connection.send_mavlink(msg)

if __name__ == "__main__":
    check_connection()
    arm_vehicle()
    
    go_to_position(0, 0, 10)
    
    time.sleep(10)
    
    disarm_vehicle()
    
    sock.close()
