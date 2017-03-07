#how to import and call functions in another file
import il227_HW3

message = "Secret Message"

e_msg = il227_HW3.encrypt(message,17947,7)

d_msg = il227_HW3.decrypt(e_msg,17947,10103)

print e_msg
print d_msg
