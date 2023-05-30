import os

with open("example-test1.txt", "r") as input:
	with open("temp.txt","w") as output:
		for line in input:
			if line[0] !='#':
				output.write(line)

os.replace ('temp.txt', 'example-test1.txt')
