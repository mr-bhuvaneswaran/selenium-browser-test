from datetime import timedelta, date


def daterange(date1, date2):
	for n in range(int((date2 - date1).days) + 1):
		yield date1 + timedelta(n)

fobj = open('pattern.txt','a+')
start_dt = date(1997, 01, 01)
end_dt = date(1998, 12, 31)
for dt in daterange(start_dt, end_dt):
	fobj.write(dt.strftime("%d/%m/%Y\n"))

