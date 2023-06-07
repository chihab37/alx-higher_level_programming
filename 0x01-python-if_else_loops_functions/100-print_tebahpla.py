#!/usr/bin/python3
output = ""

for i in range(ord('z'), ord('A') - 1, -1):
    output += "{}{}".format(chr(i), chr(i - 32) if i % 2 == 1 else chr(i - 32))
	print(output, end="")
