import sys

# check is user wants to encode
if sys.argv[1] == "-e":
    while(True):
        try:
            key = list(sys.argv[2].lower().replace(" ", "")) # remove spaces in the key
            plain_text = list(input())  # get message to encode as list
            plain = []
            cipher = []

            # convert upper case to lower case in plain_text
            for i in range(len(plain_text)):
                if (plain_text[i].isupper()):
                    plain.append(plain_text[i].lower())
                else:
                    plain.append(plain_text[i])

            # convert plain txt and key to unicode 
            for j in range(len(plain)):
                plain[j] = ord(plain[j]) - 97 # maps letters to corresponding numbers

            for k in range(len(key)):
                key[k] = ord(key[k]) - 97

            l = 0
            m = 0
            finished = False
            # encode the plain text to cipher text
            while l < len(plain):
                if l == len(plain): # if at the end of plain text, set finished to True
                            finished = True
                if finished: # if finished is true, break out current while loop
                    break
                # check to see if charcter is not a letter
                while (plain[l] < 0 or plain[l] > 25):
                    cipher.append(plain[l]) # if not, append to cipher text and move on
                    l += 1
                    if l == len(plain): # if at the end of plain text, set finished to True
                        finished = True
                        break
                if finished: # if finished is true, break out of initial while loop
                    break
                while m < len(key):
                    if l == len(plain): # if at the end of plain text, set finished to True
                            finished = True
                    if finished: # if finished is true, break out current while loop
                        break
                    # check to see if charcter is not a letter
                    while (plain[l] < 0 or plain[l] > 25):
                        cipher.append(plain[l]) # if not, append to cipher text and move on
                        l += 1
                        if l == len(plain): # if at the end of plain text, set finished to True
                            finished = True
                        if finished: # if finished is true, break out current while loop
                            break
                    if finished: # if finished is true, break out of current while loop
                        break
                    x = plain[l] + key[m]
                    if x > 25:
                        x = x % 26
                    cipher.append(x)
                    l += 1
                    m += 1
                    if l == len(plain): # if finished is true, break out current while loop
                        finished = True
                m = 0
                if finished: # if finished is true, break out of initial while loop
                    break

            message = ""
            # upper case characters that were originally upper case and convert unicode back to alphapbet
            for n in range(len(cipher)):
                if plain_text[n].isupper():
                    message += chr(cipher[n] + 97).upper()
                else:
                    message += chr(cipher[n] + 97)

            # print encoded message
            print(message)
        except:
            break


# check is user wants to decode
# Works exactly like above, but instead of encoding a message, it decodes a message
# refer to encoding section for comments on code
if sys.argv[1] == "-d":
    while(True):
        try:
            key = list(sys.argv[2].lower().replace(" ", ""))
            plain_text = list(input())
            plain = []
            cipher = []

            for i in range(len(plain_text)):
                if (plain_text[i].isupper()):
                    plain.append(plain_text[i].lower())
                else:
                    plain.append(plain_text[i])

            for j in range(len(plain)):
                plain[j] = ord(plain[j]) - 97

            for k in range(len(key)):
                key[k] = ord(key[k]) - 97

            l = 0
            m = 0
            finished = False

            while l < len(plain):
                if l == len(plain):
                            finished = True
                if finished:
                    break

                while (plain[l] < 0 or plain[l] > 25):
                    cipher.append(plain[l])
                    l += 1
                    if l == len(plain):
                        finished = True
                        break
                if finished:
                    break
                while m < len(key):
                    if l == len(plain):
                            finished = True
                    if finished:
                        break

                    while (plain[l] < 0 or plain[l] > 25):
                        cipher.append(plain[l])
                        l += 1
                        if l == len(plain):
                            finished = True
                        if finished:
                            break
                    if finished:
                        break
                    x = 26 + plain[l] - key[m]
                    if x > 25:
                        x = x % 26
                    cipher.append(x)
                    l += 1
                    m += 1
                    if l == len(plain):
                        finished = True
                m = 0
                if finished:
                    break

            message = ""

            for n in range(len(cipher)):
                if plain_text[n].isupper():
                    message += chr(cipher[n] + 97).upper()
                else:
                    message += chr(cipher[n] + 97)

            print(message)
        except:
            break
