import hashlib
import os
import ast
import getpass

# create dictionary of username & password combinations
# add any new usernames and passwords here
# index will be username and value with be a pair of (password, salt)
usr_passwd = {}

def encrypt(msg , N=17947 , E=7):
    return [ord(s)**E % N for s in msg]


# for any password, generate a salt & store the salt in the dictonary along with
# the hashed & salted password
def create_account(size=32):
    usr = raw_input("Enter username> ")
    while usr in usr_passwd:
        print "Username taken. Enter new username"
        usr = raw_input("Enter username> ")
    passwd = getpass.getpass("Enter password> ")
    salt = os.urandom(size)
    usr_passwd[usr]=(hashlib.sha512(passwd+salt).hexdigest(),salt)
    print "Account created."


# msg is an array of an array of integers
def password(msg , usr , passwd ):
    def decrypt(msg , N=17947 , D=10103):
        return "".join([chr(s**D % N) for s in msg ])

    if usr in usr_passwd:
        hashed_password,salt = usr_passwd[usr]
        if hashlib.sha512(passwd+salt).hexdigest() == hashed_password:
            for value in msg:
                printed = decrypt (value)
        else:
            printed = "Wrong username/password combination."
    else:
        printed = "Wrong username/password combination."
        return printed
# Your code that checks the username/password combination goes here

# def instant_message():
#     list_of_messages = []
#     while True:
#         var = raw_input("Insert Message> ")
#         if var=="STOP":
#             break
#         list_of_messages.append(encrypt(var))
#     return list_of_messages


def write_message():
    file_object = open("message_log.txt", "w")
    while True:
        var = raw_input("Insert Message> ")
        if var == "STOP":
            break
        file_object.write(str(encrypt(var))+ "\n")

    file_object.close()

def read_message():

    usr = raw_input("Enter username> ")
    passwd = getpass.getpass("Enter password> ")

    tempt_file = open("message_log.txt", 'r').read()
    tempt_file = tempt_file.strip()
    row_of_lines = tempt_file.split("\n")

    # row_of_lines is an array carrying strings of each line in the file
    # each line is a string representation of each array

    line_array = []
    for line in row_of_lines:
        if password(line_array,usr,passwd)=="Wrong username/password combination.":
            break
        else:
        # transform the string representation of an array into an array, line_array
            line_array.append(ast.literal_eval(line))
            password(line_array,usr,passwd)


# Test (Socrates is my cat's name :D)
# create_account("hch54", "Fifa")
# create_account("il227","Socs")

# message = "This is a secret message"
# encrypted_message = encrypt(message)
# decrypted_message = password ( encrypted_message , "hch54", "Fifa")
