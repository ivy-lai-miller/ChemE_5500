import random

# Generate random array using for loop
# nums = []
# for i in range(50):
# 	nums.append(int(random.random() * 100))
# 	nums.append(random.randint(0, 100))


# Generate random array using list comprehension
# nums = [int(random.random() * 100.0) for i in range(50)]

# print nums

# # nums.sort()
# nums = sorted(nums)

# print nums


###############################################################

nums = [(int(random.random() * 100.0), int(random.random() * 100.0)) for i in range(10)]
print nums

# nums.sort()
nums = sorted(nums, key = lambda x: x[1])
print nums
