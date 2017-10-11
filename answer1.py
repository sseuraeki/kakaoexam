import sys
import time

start_time = time.time()

assert len(sys.argv) >= 4, "Usage: python answer1.py [n] [arr1] [arr2]"
assert len(sys.argv[1]) >=1, "n must be 1 or larger"
assert len(sys.argv[1]) <= 16, "n must be 16 or smaller"

# convert system argument arrays to lists
for i in range(2, len(sys.argv)):
	if "]" in sys.argv[i]:
		arr1 = sys.argv[2:i+1]
		break

arr2 = sys.argv[i+1:]

arr1 = [x.strip("[").strip("]").strip(",").strip() for x in arr1]
arr2 = [x.strip("[").strip("]").strip(",").strip() for x in arr2]

def dec_to_bin(x):
	# decimal to binary recursive function
	if x <= 1:
		return [x]
	else:
		return dec_to_bin(x//2) + [x % 2]

def adjust_length(n, arr):
	# binary array to n length by adding 0 in front
	if len(arr) == n:
		return arr
	else:
		return adjust_length(n, [0]+arr)

def answer1(n, arr1, arr2):
	bin_arr1 = []
	bin_arr2 = []

	def helper(n, arr, bin_arr):
		for x in arr:
			x = int(x)
			assert x >= 0, "eveny element in arrays must be 0 or larger"
			assert x <= 2 ** n - 1, "eveny element in arrays must be 2 ** n - 1 or smaller"
			a = dec_to_bin(x)
			a = adjust_length(n, a)
			bin_arr.append(a)

	helper(n,arr1,bin_arr1)
	helper(n,arr2,bin_arr2)

	answer = []

	for x, y in zip(bin_arr1, bin_arr2):
		string = ""
		for i in range(n):
			if x[i] + y[i]:
				string += "#"
			else:
				string += " "
		answer.append(string)

	return answer

print(answer1(int(sys.argv[1]), arr1, arr2))

end_time = time.time()
print(end_time - start_time, " seconds elapsed")



