fobj = open('rollcse.txt','a+')

for i in range(1,121):
    fobj.write("15BCS2"+ str(i).zfill(3) + "\n")