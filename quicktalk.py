import socket
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 35001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto("\00\00\00"+chr(int(sys.argv[1]))+"ADIS\x00\x00\x00\x00\x00\x00\x00\x18\x2D\x08\x06\x00\x04\x00\xF7\xFF\x28\x01\x01\x00\x00\x00\x9F\x04\x8D\xFF\xC8\xFD\x3C\x00\x00\x00ROLL\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x01", (UDP_IP, UDP_PORT))
