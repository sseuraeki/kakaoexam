import sys
import time

start_time = time.time()

assert len(sys.argv) >= 3, "Usage: python answer3.py [cacheSize] [array]"

size = int(sys.argv[1]) # convert string system arg to int

# convert string system arg to list
cities = sys.argv[2]
if len(sys.argv) > 3:
	for i in range(3, len(sys.argv)):
		cities += sys.argv[i]

cities = cities.split(",")
cities = [x.strip("[").strip("]").strip() for x in cities]

def answer3(size, arr):
	cache = []
	duration = 0

	for i in range(len(arr)):
		if arr[i].lower() in cache:
			duration += 1
		else:
			duration += 5
		cache.append(arr[i].lower())
		cache = cache[-size:]

	return duration

print answer3(size, cities)

end_time = time.time()
print end_time - start_time, " seconds elapsed"