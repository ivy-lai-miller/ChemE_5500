import random

rand_list = [int(random.random() * 100) for i in range(50)]
rand_list.sort()

print rand_list

# > 10

# smallest_ten = 238904
# for i in range(50):
# 	if rand_list[i] > 10 and rand_list[i] < smallest_ten:
# 		smallest_ten = rand_list[i]
# print smallest_ten

for v in rand_list:
	if v > 10:
		print v
		break


# < 90

# largest = -238904
# for i in range(50):
# 	if rand_list[i] < 90 and rand_list[i] > largest:
# 		largest = rand_list[i]
# print largest

# prev = None
# for v in rand_list:
# 	if v < 90:
# 		prev = v
# 	else:
# 		break
# print prev

for v in rand_list[::-1]:
	if v < 90:
		print v
		break


# min
# print rand_list[0]
print min(rand_list)

# max
# print rand_list[-1]
print max(rand_list)
