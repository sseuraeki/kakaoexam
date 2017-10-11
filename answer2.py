import sys
import time

start_time = time.time()

assert len(sys.argv) == 2, "there must be one and only one dartResult"

def is_int(s):
	# check if s is int
	try:
		int(s)
		return True
	except:
		return False

def convert_instance(dart):
	# split string into three instances
	first = str(dart[0])
	for i in range(1,len(dart)):
		if is_int(dart[i]):
			first = first + str(dart[i])
		else:
			break
	first = [first]
	for i2 in range(i,len(dart)):
		if not is_int(dart[i2]):
			first.append(dart[i2])
		else:
			break

	second = str(dart[i2])
	for j in range(i2+1,len(dart)):
		if is_int(dart[j]):
			second = second + str(dart[j])
		else:
			break
	second = [second]
	for j2 in range(j,len(dart)):
		if not is_int(dart[j2]):
			second.append(dart[j2])
		else:
			break

	third = str(dart[j2])
	for k in range(j2+1,len(dart)):
		if is_int(dart[k]):
			third = third + str(dart[k])
		else:
			break
	third = [third] + [x for x in dart[k:]]

	return first, second, third

def prize(instance):
	if instance[-1] == "#":
		return -1
	elif instance[-1] == "*":
		return "*"
	else:
		return 1

def score(instance):
	if instance[-1] =="S" or instance[-2] == "S":
		return int(instance[0])
	elif instance[-1] =="D" or instance[-2] == "D":
		return int(instance[0]) ** 2
	else:
		return int(instance[0]) ** 3

def answer2(dart):
	a,b,c = convert_instance(dart)
	scores = [score(x) for x in [a,b,c]]
	prizes = [prize(x) for x in [a,b,c]]

	total = []

	for i in range(3):
		if i == 0 and prizes[i] == "*":
			total.append(scores[0] * 2)
		else:
			if prizes[i] == "*":
				total.append(total[i-1] + scores[i] * 2)
			else:
				total.append(scores[i] * prizes[i])

	return sum(total)

print(answer2(sys.argv[1]))

end_time = time.time()
print(end_time - start_time, " seconds elapsed")
