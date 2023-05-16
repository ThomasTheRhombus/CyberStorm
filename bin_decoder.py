import fileinput

# this function converts a binary number to a decimal number
def binary_to_dec(binary):
    binary = int(binary)
    decimal = 0
    place = 0
    while binary != 0:
        bit = binary % 2
        binary = binary // 10
        if bit == 1:
            decimal += 2**place
        place+=1
    return decimal

# read the file given in terminal
for fileinput_line in fileinput.input():
    binary = fileinput_line

# convert the text to an integer
binary = int(binary)
# make a copy of the binary integer
binary_copy = binary

# create an output string to add to and return later
output = ""

# 7-bit ASCII
while binary != 0:
    # create a 'byte' string to edit
    byte = ""
    for i in range(7):
        bit = binary % 2    # determine the lsb
        byte += str(bit)    # add it to 'byte' string
        binary //= 10       # move to next lsb

    byte = byte [::-1] # reverse 'byte' string

    # convert the byte to its ASCII representation and add it to the output string
    output += chr(binary_to_dec(byte))

# reverse the output string
output = output[::-1]

# print output
print(output)

print("----------------------------------------------------")

# create an output string to add to and return later
output = ""

# 8-bit ASCII
# works the same way as 7-bit ASCII above but for 8-bit ASCII
while binary_copy != 0:
    byte = ""
    for i in range(8):
        bit = binary_copy % 2
        byte += str(bit)
        binary_copy //= 10

    byte = byte [::-1]

    output += chr(binary_to_dec(byte))

output = output[::-1]

print(output)