#Generate strong random passwords

import random
import string

#Define the length of the password
word_length = 18

#Generating a list of letters, digits, and some punctuation
components = [string.ascii_letters, string.digits, "!@#$%&"]

chars = []

for clist in components:
    for item in clist:
        chars.append(item);

def generate_password():
    #storing the password
    password = []

    #choose a random item from chars and add it to password
    for i in range(word_length):
        rchar = random.choice(chars)
        password.append(rchar)

    #return the password as a string
    return "".join(password)

#Output generated password
print(generate_password())
