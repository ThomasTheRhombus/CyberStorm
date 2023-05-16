from hashlib import md5
from datetime import datetime, timezone
import fileinput

chars = ['a','b','c','d','e','f']
nums = ['1','2','3','4','5','6','7','8','9']

DEBUGGING = False # Testing variable. Can be removed in final submission

if(not DEBUGGING):
    current_date = datetime.now() # get current time
    for fileinput_line in fileinput.input(): # read epoch time from input "yyyy mm dd hh MM ss"
        epoch_str = fileinput_line
    epoch_str = epoch_str.split()   # split string at spaces and make array
    # create epoch date with given epoch time
    epoch_date = datetime(int(epoch_str[0]),int(epoch_str[1]),int(epoch_str[2]),int(epoch_str[3]),int(epoch_str[4]),int(epoch_str[5]))

if(DEBUGGING): # if DEBUGGING/Testing, you can mannually set current date and epoch date. Whole block and be removed in final submission
    current_date = datetime(2017,4,23,18,2,30)
    epoch_date = datetime(1999,12,31,23,59,59)

# adjust dates to UTC time zone (accounts for daylight savings)
current_date = current_date.astimezone(timezone.utc)
epoch_date = epoch_date.astimezone(timezone.utc)

# calculate difference in dates
deltatime = current_date - epoch_date

# change to seconds
seconds = deltatime.total_seconds()
# find the start of 60 second interval
seconds = str(int(seconds - (seconds % 60)))

# hash the number twice and return hex representation
hash_str = md5(((md5(seconds.encode())).hexdigest()).encode()).hexdigest()

code = ""   # create empty code string to append to
count = 0
index = 0

# starting from left, find first 2 characters and append code
while count != 2:
    if hash_str[index] in chars:
        code += hash_str[index]
        count+=1
    index += 1

# starting from rifght, find first 2 numbers and append code
index = 31
while count != 4:
    if hash_str[index] in nums:
        code += hash_str[index]
        count+=1
    index -= 1

# print code
print(code)