def calculate():
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$&_?/%"
    fobj = open('master.txt','a+')
    for i in s:
        for n in range(8):
            check = i * 8
            for j in s:
                temp = list(check)
                temp[n] = j
                check= ''.join(temp)
                fobj.write(check+"\n")


if __name__ == '__main__':
    calculate()
