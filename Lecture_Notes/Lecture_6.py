ex_dict = {"elem1":4}

ex_dict["elem2"] = 5

sample_dict = {}
for value in range(4,344):
    sample_dict[value]=str(value)

# print sample_dict

#prints a five times
a = [4]*5

# not the same
# a2 creates four lists at the same address (say x1)
# b creates four lists at four different addresses
a2 = [[4]]*5
b = [[4]for i in range(5)]

# a2[3] is a pointer
a2[3].append(3)
# b[3] is a list
b[3].append(3)

# print a2
# print b


# Syntax of a class: (constants and classes should be capital)
class Example:
    # a = 3
    # b = 4

    # initializing function, need to use __init__
    def __init__(self,a,b):
        self.aval = a
        self.bval = b

    def sum(self):
        return self.aval+self.bval

    def multiply(self):
        return self.aval * self.bval


test = Example(3,2)
# print test.multiply()






class Node:
    next_node = None
    prev_node = None
    value = None

    def prnt(self):
        print self.value


a = Node()
a.value = 3
a.prnt()

# make a linked list
root = Node()
child = Node()
root.next_node = child
child.prev_node = root
root.value = 989080
child.value = 123

root.prnt()
child.prnt()
root.next_node.prnt() #should be 123
child.prev_node.prnt() # should be 98080
