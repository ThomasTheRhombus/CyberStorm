import sys

key = 'key2' # define the key

bytes_key = bytearray(open(key,'rb').read()) # read the key and reate bytearray
bytes_input = bytearray(sys.stdin.buffer.read()) # read the input and create bytearray
bytes_output = bytearray()  # create empty bytearray for output

for x in range(len(bytes_input)): # for each byte in input
    bytes_output.append((bytes_key[x] ^ bytes_input[x])) # XOR input and key and append to ouput

sys.stdout.buffer.write(bytes_output) # print output