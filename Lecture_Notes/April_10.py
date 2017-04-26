import random

# # list comprehension to make an array of ints from range 0 to 100
# nums = [random.randint(0,100) for x in range(50)]
#
# # nums.sort()
# nums = sorted(nums)
# # print nums
#
#
# # Now make a random list of tuples
#
# nums = [(random.randint(0,100),random.randint(0,100)) for x in range(10)]
# # sorts by the second index (not the first)
# nums = sorted(nums, key = lambda x: x[1])
# print nums

rand_list = [int(random.random()*100) for i in range(50)]

print rand_list
# Find index of smalllest value larger than 10

rand_list = sorted(rand_list)
print rand_list

#Find smallest value
print "Smallest value is %d" %rand_list[0]
# print min(rand_list)

# Find largest value
print "Largest value is %d" %rand_list[-1]

start = len(rand_list)/2

# start at the halfway and check if it is less

for x in rand_list:
    if x > 10:
        print "Smallest value greater than 10 is %d" %x
        break

for x in rand_list[::-1]:
    if x < 90:
        print "Largest value less than 90 is %d" %x
        break
