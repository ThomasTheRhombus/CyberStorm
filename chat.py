from socket import *
from sys import stdout
from time import time

ip = "138.47.99.64" # ip you want to connect to
#ip = "localhost"
port = 31337

ZERO = 0.025
ONE = 0.075

s = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM -> use TCP

s.connect((ip, port))

data = s.recv(4096).decode()

covert_bin = ""

while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    delta = round(t1-t0, 3)
    if (delta >= ONE):
        covert_bin += '1'
    else:
        covert_bin += '0'    

s.close()

covert_str = ""

for i in range(0, len(covert_bin), 8):
    covert_str += chr(int(f'0b{covert_bin[i:i+8]}',2))

message = covert_str.split("EOF")


print(f"Covert Message:\n{message[0]}")
