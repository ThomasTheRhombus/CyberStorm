import sys
from time import sleep

SENTINEL = bytearray([0x00,0xff,0x00,0x00,0xff,0x00])

try:
    test = sys.argv[1]
except:
    print(f"{sys.argv[0]} Usage: {sys.argv[0]} -(sr) -(bB) [-o<val>] [-i<val>] -w<val> -h<val>")
    exit()

if sys.argv[1] == "-s":
    storing = True
    retrieving = False
elif sys.argv[1] == "-r":
    retrieving = True
    storing = False
else:
    print(f"{sys.argv[0]} Usage: {sys.argv[0]} -(sr) -(bB) [-o<val>] [-i<val>] -w<val> -h<val>")
    exit()

if sys.argv[2] == "-b":
    bit_method = True
    byte_method = False
elif sys.argv[2] == "-B":
    byte_method = True
    bit_method = False
else:
    print(f"{sys.argv[0]} Usage: {sys.argv[0]} -(sr) -(bB) [-o<val>] [-i<val>] -w<val> -h<val>")
    exit()

if sys.argv[3][:2] == "-o":
    offset = int(sys.argv[3][2:])
    if sys.argv[4][:2] == "-i":
        interval = int(sys.argv[4][2:])
        wrapper = bytearray(open(sys.argv[5][2:],'rb').read())
        if(not retrieving):
            hidden = bytearray(open(sys.argv[6][2:],'rb').read())
        else:
            hidden = bytearray()
    else:
        interval = 1
        wrapper = bytearray(open(sys.argv[4][2:],'rb').read())
        if(not retrieving):
            hidden = bytearray(open(sys.argv[5][2:],'rb').read())
        else:
            hidden = bytearray()
elif sys.argv[3][:2] == "-i":
    offset = 0
    interval = int(sys.argv[3][2:])
    wrapper = bytearray(open(sys.argv[4][2:],'rb').read())
    if(not retrieving):
        hidden = bytearray(open(sys.argv[5][2:],'rb').read())
    else:
        hidden = bytearray()
elif sys.argv[3][:2] == "-w":
    offset = 0
    interval = 1
    wrapper = bytearray(open(sys.argv[3][2:],'rb').read())
    if(not retrieving):
        hidden = bytearray(open(sys.argv[4][2:],'rb').read())
    else:
        hidden = bytearray()
else:
    print(f"{sys.argv[0]} Usage: {sys.argv[0]} -(sr) -(bB) [-o<val>] [-i<val>] -w<val> -h<val>")
    exit()

if(byte_method and storing):
    i = 0
    while(i < len(hidden)):         # for each byte in hiddem
        wrapper[offset] = hidden[i] # insert hidden byte into wrapper
        offset += interval          # move down wrapper
        i += 1

    # insert SENTINEL into wrapper after hidden
    i = 0
    while(i < len(SENTINEL)):
        wrapper[offset] = SENTINEL[i]
        offset += interval
        i += 1

elif(byte_method and retrieving):
    buffer = bytearray()                # create an empty bytearray to use as a buffer
    while(offset < len(wrapper)):       # while offset is stil within wrapper size
        buffer.append(wrapper[offset])  # add a byte from the wrapper to the buffer
        if(((len(buffer)) % 6) == 0):   # check if the buffer is 6 bytes long
            if(buffer == SENTINEL):     # if the buffer equals the SENTINEL, print the hidden file and exit
                sys.stdout.buffer.write(hidden)
                exit()
            else:                       #else append the first byte in the buffer to the hidden file and remove it from the buffer
                hidden.append(buffer[0])
                del buffer[0]
        offset += interval              # increnent the offset
    sys.stdout.buffer.write(hidden)

if(bit_method and storing):
    i = 0
    while(i < len(hidden)):
        for _ in range(8):  # for each bit in each byte
            wrapper[offset] &= 0b11111110 # clear lsb in wrapper byte
            wrapper[offset] |= (hidden[i] & 0b10000000 >> 7) # isolate first bit in hidden byte and put in lsb of wrapper byte
            hidden[i] <<= 1 # change msb to the next msb in hidden bytes
            offset += interval  # change wrapper bytes
        i += 1

    # insert SENTINEL into wrapper
    i = 0
    while(i < len(SENTINEL)):
        for _ in range(8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
            SENTINEL[i] <<= 1
            offset += interval
        i += 1
    
        

elif(bit_method and retrieving):
    buffer = bytearray()
    while(offset < len(wrapper)):
        b = 0b00000000
        for x in range(8):
            b |= (wrapper[offset] & 0b00000001)
            if(x < 7):
                b <<= 1
                offset += interval
        buffer.append(b)
        if(((len(buffer)) % 6) == 0):   # check if the buffer is 6 bytes long
            if(buffer == SENTINEL):     # if the buffer equals the SENTINEL, print the hidden file and exit
                sys.stdout.buffer.write(hidden)
                exit()
            else:                       #else append the first byte in the buffer to the hidden file and remove it from the buffer
                hidden.append(buffer[0])
                del buffer[0]
        offset += interval
    
    sys.stdout.buffer.write(hidden)
        