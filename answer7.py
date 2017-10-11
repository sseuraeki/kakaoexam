import sys
import datetime
import time

start_extime = time.time()

log = sys.argv[1]
if len(sys.argv) > 2:
	for i in range(2, len(sys.argv)):
		log += sys.argv[i]

log = log.split(",")
log = [x.strip("[").strip("]") for x in log]

def answer7(log):
	instances = []
	for instance in log:
		instance = instance.split(" ")
		end_time = datetime.datetime.strptime(instance[1], "%H:%M:%S.%f")
		interval = float(instance[2].strip("s")) - 0.001
		start_time = end_time - datetime.timedelta(seconds=interval)
		instances.append([start_time, end_time])

	intervals = []
	for instance in instances:
		count_instances = 0
		interval_start = instance[1]
		interval_end = instance[1] + datetime.timedelta(seconds=1)
		for instance in instances:
			if instance[0] < interval_end and instance[1] >= interval_start:
				count_instances += 1
		intervals.append(count_instances)

	return max(intervals)

print(answer7(log))

end_extime = time.time()
print(end_extime - start_extime, " seconds elapsed")