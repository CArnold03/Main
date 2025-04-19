fhand=open('ints.txt')
i=0
for line in fhand:
    if i==8:
        break
    i=i+1
    print(line)
