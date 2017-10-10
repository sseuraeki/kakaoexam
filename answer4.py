import sys
import datetime

assert len(sys.argv) >= 4, "Usage: python answer4.py [n] [t] [m] [timetable]"

# convert system arg timetable to datetime list
timetable = sys.argv[4]
if len(sys.argv) > 5:
	for i in range(5, len(sys.argv)):
		timetable += sys.argv[i]
timetable = timetable.split(",")
timetable = [x.strip("[").strip("]").strip() for x in timetable]
timetable = [datetime.datetime.strptime(x, "%H:%M") for x in timetable]

def answer4(n, t, m, timetable):
	start = datetime.datetime.strptime("09:00", "%H:%M")

	for i in range(n):
		deadline = start + datetime.timedelta(minutes=i*t) 
		safe = [case for case in timetable if case <= deadline]
		safe.sort()
		safe = safe[:m]
		timetable.sort()
		timetable = timetable[len(safe):]

	if len(safe) < m:
		answer = deadline
	else:
		answer = max(safe) - datetime.timedelta(minutes=1)

	return datetime.datetime.strftime(answer,"%H:%M")

n = int(sys.argv[1])
t = int(sys.argv[2])
m = int(sys.argv[3])

print(answer4(n, t, m, timetable))
