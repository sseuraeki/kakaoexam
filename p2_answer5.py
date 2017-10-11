import sys
import time

start_time = time.time()

assert len(sys.argv) >= 2, "Usage: python answer5.py [str1] [str2]"

# convert second system arg to one str
str2 = sys.argv[2]
if len(sys.argv) > 3:
	for i in range(3, len(sys.argv)):
		str2 += " " + sys.argv[i]

def convert_to_list(string):
	array = []
	for i in range(len(string)-1):
		if string[i].isalpha() and string[i+1].isalpha() and string[i] != " " and string[i+1] != " ":
			x = string[i] + string[i+1]
			array.append(x.lower())
	return array

def jacard(str1, str2):
	arr1 = convert_to_list(str1)
	arr2 = convert_to_list(str2)

	inner = []
	outer = arr1+arr2

	if len(outer) == 0:
		return 65536

	inner = [element for element in arr1 if element in arr2]

	for element in inner:
		outer.remove(element)

	return int(len(inner) / len(outer) * 65536)

print jacard(sys.argv[1], str2)

end_time = time.time()
print end_time - start_time, " seconds elapsed"