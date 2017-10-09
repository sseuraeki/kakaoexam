
def dec_to_bin(x):
	if x == 1:
		return [1]
	else:
		return dec_to_bin(x//2) + [x % 2]

def adjust_length(n, arr):
	if len(arr) == n:
		return arr
	else:
		return adjust_length(n, [0]+arr)




def answer1(n, arr1, arr2):
	bin_arr1 = []
	bin_arr2 = []

	def helper(n, arr, bin_arr):
		for x in arr:
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





