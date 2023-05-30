import sys

nums = [0]

for i in sys.argv[1:]:
	nums.append(int(i))

print (sum(nums))
