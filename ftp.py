from ftplib import FTP
import sys

# if comamnd line argument is given, use that method, else use the one provided below
try:
    METHOD = int(sys.argv[1])
except:
     METHOD = 7

# FTP server details
IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = f"{METHOD}/"
USE_PASSIVE = True # set to False if the connection times out

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

# This function converts binary to its 7-bit ascii representation
def ascii7(bin_int):
	output = ""
	# 7-bit ASCII
	while bin_int != 0:
    	# create a 'byte' string to edit
		byte = ""
		for i in range(7):
			bit = bin_int % 2    # determine the lsb
			byte += str(bit)    # add it to 'byte' string
			bin_int //= 10       # move to next lsb

		byte = byte [::-1] # reverse 'byte' string

    	# convert the byte to its ASCII representation and add it to the output string
		output += chr(binary_to_dec(byte))
	# reverse the output string
	output = output[::-1]

	# print output
	print(output)


# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

# Create empty string that will eventually hold binary
bin_string = ""

# 10 bit Method
if METHOD == 10:

	# Check each file
    for f in files:
        permissions = f[:10] # Look at only the permissions part
		# convert permissions to binary values
        for i in permissions: 
            if i != '-':
                bin_string += "1"
            else:
                bin_string += "0"

if METHOD == 7:
	# Check each file
    for f in files:
        permissions = f[:10] # Look at inly the permissions

        if permissions[:3] == "---": # filter out noise
            permissions = permissions[3:10] # remove the '---'
            # convert permissions to binary values
            for i in permissions:
                if i != '-':
                    bin_string += "1"
                else:
                    bin_string += "0"

# converty binary to 7-bit ASCii
ascii7(int(bin_string))
