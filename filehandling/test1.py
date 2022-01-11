f=open('one.txt','r')
wc = 0
cc=0
for line in f:
    word = line.split()
    wc = wc+len(word)
    cc=cc+len(line)


    print(wc)
    print((cc))

