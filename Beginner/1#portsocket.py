#port-scanner with python coding for absolute beginner 
#In this code when run it will show which port basically open 
import socket
target = input("enter ip address to scan: ")
for port in range (20, 1025):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"port {port} is OPEN")
        s.close()
